import sys
import os
import re
import subprocess

# cd ~/.cache/bazel/_bazel_penglei/d66deb4a90c8204388d168e10d497629/external
# ln -s /data/workroom/nighthawk.git/.ycm_extra_conf.py

custom_dep_top = '/data/workroom/nighthawk.git'
def generate_bazel_external(dirs):
    results = []
    for item in dirs:
      results.append(os.path.join("bazel-nighthawk.git/external", item))
    return results

custom_includes_dirs = generate_bazel_external([
    "com_google_absl",
    "envoy/include",
    "envoy/source",
    "com_github_cyan4973_xxhash",
    "com_envoyproxy_protoc_gen_validate",
    "com_google_protobuf/src",
]) + [
    "bazel-nighthawk.git",
    "bazel-genfiles",
    "source",
    "include",
]

enable_following_dir = False
_SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.m', '.mm', '.inc' ]

def LoadCustomIncludes():
  custom_includes_flags = []
  for item in custom_includes_dirs:
    if item.startswith("/"):
      item_abs_path = item
    else:
      item_abs_path = os.path.join(custom_dep_top, item)

    if os.path.isdir(item_abs_path):
      custom_includes_flags.append("-I")
    else:
      custom_includes_flags.append("-include")

    custom_includes_flags.append(os.path.normpath(item_abs_path))
  return custom_includes_flags


def LoadSystemIncludes():
  regex = re.compile('(?:\#include \<...\> search starts here\:)(?P<list>.*?)(?:End of search list)', re.DOTALL)
  process = subprocess.Popen(['clang', '-v', '-E', '-x', 'c++', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  process_out, process_err = process.communicate('')
  output = process_out + process_err
  includes = []
  if sys.version_info > (3, 0):
      newline = "\\n"
  else:
      newline = "\n"
  for p in re.search(regex, str(output)).group('list').split(newline):
    p = p.strip()
    if len(p) > 0 and p.find('(framework directory)') < 0:
      includes.append('-isystem')
      includes.append(os.path.normpath(p))
  return includes

system_includes_flags = LoadSystemIncludes()
custom_includes_flags = LoadCustomIncludes()

general_flags = [
    '-Wall',
    '-Wextra',
    '-std=c++14',
    '-x',
    'c++',
]

flags = general_flags + system_includes_flags + custom_includes_flags


def _IsHeaderFile( filename ):
  extension = os.path.splitext( filename )[ 1 ]
  return extension in [ '.h', '.hxx', '.hpp', '.hh' ]


def _FindCorrespondingSourceFile( filename ):
  if _IsHeaderFile( filename ):
    basename = os.path.splitext( filename )[ 0 ]
    for extension in _SOURCE_EXTENSIONS:
      replacement_file = basename + extension
      if os.path.exists( replacement_file ):
        return replacement_file
  return filename

def Settings(**kwargs):
  if kwargs[ 'language' ] == 'cfamily':
    filename = _FindCorrespondingSourceFile( kwargs['filename'] )
    resultSettings = {
      'flags': flags,
      'override_filename': filename
    }
    if enable_following_dir:
      resultSettings['include_paths_relative_to_dir'] = DIR_OF_THIS_SCRIPT
    return resultSettings

  return {}

def _GetStandardLibraryIndexInSysPath( sys_path ):
  for path in sys_path:
    if os.path.isfile( os.path.join( path, 'os.py' ) ):
      return sys_path.index( path )
  raise RuntimeError( 'Could not find standard library path in Python path.' )


def PythonSysPath( **kwargs ):
  sys_path = kwargs[ 'sys_path' ]
  dir_of_third_party = os.path.join('~/.vim/plugged/YouCompleteMe/third_party' )
  for folder in os.listdir(dir_of_third_party):
    if folder == 'python-future':
      folder = os.path.join( folder, 'src' )
      sys_path.insert( _GetStandardLibraryIndexInSysPath( sys_path ) + 1,
                       os.path.realpath( os.path.join( dir_of_third_party, folder)))
      continue

    if folder == 'cregex':
      interpreter_path = kwargs[ 'interpreter_path' ]
      major_version = subprocess.check_output( [
        interpreter_path, '-c', 'import sys; print( sys.version_info[ 0 ] )' ]
      ).rstrip().decode( 'utf8' )
      folder = os.path.join( folder, 'regex_{}'.format( major_version ) )

    sys_path.insert( 0, os.path.realpath( os.path.join(dir_of_third_party, folder)))
  return sys_path

if __name__ == '__main__':
  for s in (system_includes_flags + custom_includes_flags):
    if not s.startswith('-'):
      print(s)


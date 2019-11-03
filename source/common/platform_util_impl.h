#pragma once

#include <pthread.h>

#include <thread>

#include "nighthawk/common/platform_util.h"
#if defined(__APPLE__)
#define pthread_yield() pthread_yield_np()
#endif
namespace Nighthawk {

using namespace std::chrono_literals;

class PlatformUtilImpl : public PlatformUtil {
public:
  void yieldCurrentThread() const override { pthread_yield(); }
  void sleep(std::chrono::microseconds duration) const override {
    std::this_thread::sleep_for(duration); // NO_CHECK_FORMAT(real_time)
  };
};

} // namespace Nighthawk

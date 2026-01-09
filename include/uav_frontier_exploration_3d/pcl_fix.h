// Workaround for PCL 1.10 lambda type mismatch errors with C++11
// This file should be included instead of the problematic PCL headers

#ifndef PCL_FIX_H_
#define PCL_FIX_H_

// Suppress all warnings from PCL headers
#pragma GCC system_header

#include <pcl/point_types.h>
#include <pcl/conversions.h>
#include <pcl/io/pcd_io.h>
#include <pcl_ros/transforms.h>
#include <pcl/filters/passthrough.h>
#include <pcl/filters/extract_indices.h>
#include <pcl_conversions/pcl_conversions.h>

#endif // PCL_FIX_H_

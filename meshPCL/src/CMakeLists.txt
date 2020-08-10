cmake_minimum_required(VERSION 3.5.1 FATAL_ERROR)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# FOR C++ VERSIONING
#project(pcl_visualizer_viewports)
#add_executable (check_demo new.cpp)

# FOR VISUALIZER PROJECT
#find_package(PCL 1.9 REQUIRED)
#include_directories(${PCL_INCLUDE_DIRS})
#link_directories(${PCL_LIBRARY_DIRS})
#add_definitions(${PCL_DEFINITIONS})
#add_executable (pcl_visualizer_demo pcl_visualizer.cpp)
#target_link_libraries (pcl_visualizer_demo ${PCL_LIBRARIES})

# FOR MAIN PROJECT
project(pcd_write)
find_package(PCL 1.9 REQUIRED)
include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})
set(MAIN_SOURCE "main.cpp")
add_executable(${PROJECT_NAME} ${MAIN_SOURCE})
target_link_libraries(${PROJECT_NAME} ${PCL_LIBRARIES})
message("=========================================")
message("Project: ${PROJECT_NAME} COMPILED WITH CMAKE " ${CMAKE_VERSION})
message("=========================================")

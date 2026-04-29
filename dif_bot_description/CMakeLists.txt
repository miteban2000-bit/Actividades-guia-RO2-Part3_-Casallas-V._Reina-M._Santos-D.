cmake_minimum_required(VERSION 3.5)
project(dif_bot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY activity4/launch
  DESTINATION share/${PROJECT_NAME}/
)

install(DIRECTORY activity4/urdf
  DESTINATION share/${PROJECT_NAME}/
)

install(DIRECTORY activity4/rviz
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()

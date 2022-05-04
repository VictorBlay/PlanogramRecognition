#!/bin/bash

cd mediapipe_master
FILES_DIR="../templates"
INDEX_FILENAME= "../knift_index"

echo "Extracting features from $FILES_DIR directory"
bazel-bin/mediapipe/examples/desktop/template_matching/template_matching_tflite \
--calculator_graph_config_file=mediapipe/graphs/template_matching/index_building.pbtxt \
--input_side_packets="file_directory=$FILES_DIR,file_suffix=jpg,output_index_filename=$INDEX_FILENAME"
echo "Features extracted in $INDEX_FILENAME"
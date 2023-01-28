from scenedetect import SceneManager, VideoManager
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg

#def find_scenes_save_video(video_path):
    # Create our video & scene managers, then add the detector.
video_path = "/Users/haizhouli/Documents/BU/Fall2022/CS622/Video_search/flask_search/static/0.mp4"
video_manager = VideoManager([video_path])
scene_manager = SceneManager()
scene_manager.add_detector(ContentDetector())

    # Improve processing speed by downscaling before processing.
video_manager.set_downscale_factor()

    # Start the video manager and perform the scene detection.
video_manager.start()
scene_manager.detect_scenes(frame_source=video_manager)

    # Save the video
scene_list = scene_manager.get_scene_list()
for index, scene in enumerate(scene_list):
    split_video_ffmpeg([video_path], [scene],
                        f"{index + 1}.mp4", "", suppress_output=True)


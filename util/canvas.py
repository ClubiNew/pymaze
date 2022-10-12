from PIL import Image
import os

class Canvas():
    _frames: list[Image.Image] = []
    _path_count: int = 0
    _canvas: Image.Image

    def __init__(self, size_x: int, size_y: int, scale: int, save_frames: bool):
        self.size_x = size_x
        self.size_y = size_y
        self.scale = scale
        self.save_frames = save_frames
        # initialize canvas
        self._canvas = Image.new('1', (size_x, size_y))
        for x in range(1, size_x, 2):
            for y in range(1, size_y, 2):
                # paths are at odd co-ordinates
                self._canvas.putpixel((x, y), 1)

    def _resize(self, img: Image.Image) -> Image.Image:
        size = (self.size_x * self.scale, self.size_y * self.scale)
        return img.resize(size)

    def path(self, x: int, y: int):
        self._canvas.putpixel((x,y), 1)
        if self.save_frames:
            self._frames.append(self._canvas.copy())

    def preview(self):
        self._resize(self._canvas).show()

    def save(self, file_name: str):
        if not os.path.isdir("out"):
            os.makedirs("out")
        self._resize(self._canvas).save(f"out/{file_name}.png")

    def save_animated(self, file_name: str, fps: int, duration: int):
        frames_required = fps * (duration - 2)
        frame_skip = max(len(self._frames) // frames_required, 1)
        resized_frames: list[Image.Image] = []

        for frame in self._frames[::frame_skip]:
            resized_frames.append(self._resize(frame).convert('P'))

        # show result for 2 seconds
        final_frame = self._resize(self._canvas).convert('P')
        resized_frames += [final_frame] * (fps * 2)

        frame_length = duration * 1000 / len(resized_frames)
        resized_frames[0].save(
            f"out/{file_name}.gif", duration=frame_length,
            save_all=True, optimize=True, loop=True,
            append_images=resized_frames[1:]
        )

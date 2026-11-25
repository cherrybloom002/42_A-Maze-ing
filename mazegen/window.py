from mlx import Mlx


def mykey(keynum, stuff):
    if keynum == 65307:
        m.mlx_destroy_window(mlx_ptr, win_ptr)
        m.mlx_loop_exit(mlx_ptr)


m = Mlx()
stuff = 0
mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 640, 360, "A_Maze_ing!")
m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")
m.mlx_key_hook(win_ptr, mykey, stuff)
m.mlx_loop(mlx_ptr)
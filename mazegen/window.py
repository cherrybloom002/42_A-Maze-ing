from mlx import Mlx


def mykey(keynum, mystuff):
    print(f"Got key {keynum}, and got my stuff back:")
    print(mystuff)
    if keynum == 65307:
        m.mlx_destroy_window(mlx_ptr, win_ptr)
        m.mlx_loop_exit(mlx_ptr)


def close_window(param):
    exit(0)
    return(0)


#def main() -> None:
m = Mlx()
mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 200, 200, "test")
m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 255, "Hello PyMlx!")

stuff = [1, 2]
m.mlx_hook(win_ptr, 17, 0, close_window, None)
m.mlx_key_hook(win_ptr, mykey, stuff)
m.mlx_loop(mlx_ptr)
m.mlx_destroy_window(mlx_ptr, win_ptr)
m.mlx_on


#if __name__ == "__main__":
    #main()
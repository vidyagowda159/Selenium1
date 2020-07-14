from settings import wd,url

class chromePage():

    def browserCommands(self):
        wd.get(url)
        titleName = print(wd.title)
        print(wd.current_url)
        print(wd.get_window_position())
        print(wd.get_window_size())
        print(wd.get_window_rect())
        position=wd.get_window_position()
        print(position)
        updated_pos=wd.set_window_position(position['x']+100,position['y']+200)
        print(updated_pos)
        wd.refresh()
        import time
        time.sleep(3)
        wd.back()
        wd.forward()
        print(wd.name)
        print(wd.page_source)
        wd.set_page_load_timeout(10)
        wd.fullscreen_window()
        wd.close()

obj=chromePage()
obj.browserCommands()
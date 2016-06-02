""" Façade
Makes an interface simpler

Created: 10:01 PM Wednesday, June 01, 2016
"""
class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

class HomeTheaterFacade(LogObject):
    def watch_movie(self):      pass
    def end_movie(self):        pass
    def listen_to_cd(self):     pass
    def end_cd(self):           pass
    def listen_to_radio(self):  pass
    def end_radio(self):        pass


# Complex system
class Amplifier(LogObject):
    def __init__(self):
        super().__init__()
        self.tuner = Tuner()
        self.dvdplayer = DVDPlayer()
        self.cdplayer = CDPlayer()

    def on(self):                   pass
    def off(self):                  pass
    def set_cd(self):               pass
    def set_dvd(self):              pass
    def set_stereo_sound(self):     pass
    def set_tuner(self):            pass
    def set_volume(self):           pass


class Tuner(LogObject):
    def __init__(self):
        super().__init__()
        self.amplifier = Amplifier()

    def on(self):                   pass
    def off(self):                  pass
    def set_am(self):               pass
    def set_fm(self):               pass
    def set_frequency(self):        pass


class DVDPlayer(LogObject):
    def __init__(self):
        super().__init__()
        self.amplifier = Amplifier()

    def on(self):                       pass
    def off(self):                      pass
    def eject(self):                    pass
    def pause(self):                    pass
    def play(self):                     pass
    def set_surround_audio(self):       pass
    def set_two_channel_audio(self):    pass
    def stop(self):                     pass


class CDPLayer(LogObject):
    def __init__(self):
        super().__init__()
        self.amplifier = Amplifier()

    def on(self):       pass
    def off(self):      pass
    def eject(self):    pass
    def pause(self):    pass
    def play(self):     pass
    def stop(self):     pass


class Screen(LogObject):
    def up(self):       pass
    def down(self):     pass


class PopcornPopper(LogObject):
    def on(self):       pass
    def off(self):      pass
    def pop(self):      pass

class TheaterLights(LogObject):
    def on(self):       pass
    def off(self):      pass
    def dim(self):      pass


class Projector(LogObject):
    def __init__(self):
        super().__init__()
        self.dvdplayer = DVDPlayer()

    def on(self):               pass
    def off(self):              pass
    def tv_mode(self):          pass
    def widescreen_mode(self):  pass




# Configure Log
class AppLog:
    class __AppLog:
        def __init__(self):
            self.log = logging.getLogger(__name__)
            h = logging.StreamHandler(sys.stdout)
            f = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
            h.setFormatter(f)
            self.log.setLevel(logging.DEBUG)
            self.log.addHandler(h)

    instance = None

    def __init__(self):
        if not AppLog.instance:
            AppLog.instance = self.__AppLog()


    def __getattr__(self, attr):
        return getattr(self.instance, attr)


# Define tests
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = AppLog().log

    def test_case_01(self):
      pass

  def test_case_02(self):
      pass


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))

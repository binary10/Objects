""" Façade
Makes an interface simpler

Created: 10:01 PM Wednesday, June 01, 2016
"""
class LogObject:
    def __init__(self):
        self.log = logging.getLogger('.'.join([__name__, type(self).__name__]))

class HomeTheaterFacade(LogObject):
    def __init__(self,
                amp,
                tuner,
                dvdplayer,
                cdplayer,
                projector,
                screen,
                theaterlights,
                popcornpopper):
        self.amp            = amp
        self.tuner          = tuner
        self.dvdplayer      = dvdplayer
        self.cdplayer       = cdplayer
        self.projector      = projector
        self.screen         = screen
        self.theaterlights  = theaterlights
        self.popcornpopper  = popcornpopper
        
                
    def watch_movie(self):      self.log.info('')
    def end_movie(self):        self.log.info('')
    def listen_to_cd(self):     self.log.info('')
    def end_cd(self):           self.log.info('')
    def listen_to_radio(self):  self.log.info('')
    def end_radio(self):        self.log.info('')


# Complex system
class Amplifier(LogObject):
    def __init__(self):
        super().__init__()
        self.tuner = Tuner(self)
        self.dvdplayer = DVDPlayer(self)
        self.cdplayer = CDPLayer(self)

    def on(self):                   self.log.info('')
    def off(self):                  self.log.info('')
    def set_cd(self):               self.log.info('')
    def set_dvd(self):              self.log.info('')
    def set_stereo_sound(self):     self.log.info('')
    def set_tuner(self):            self.log.info('')
    def set_volume(self):           self.log.info('')


class Tuner(LogObject):
    def __init__(self, amplifier = None):
        super().__init__()
        self.amplifier = amplifier

    def on(self):                   self.log.info('')
    def off(self):                  self.log.info('')
    def set_am(self):               self.log.info('')
    def set_fm(self):               self.log.info('')
    def set_frequency(self):        self.log.info('')


class DVDPlayer(LogObject):
    def __init__(self, amplifier = None):
        super().__init__()
        self.amplifier = amplifier

    def on(self):                       self.log.info('')
    def off(self):                      self.log.info('')
    def eject(self):                    self.log.info('')
    def pause(self):                    self.log.info('')
    def play(self):                     self.log.info('')
    def set_surround_audio(self):       self.log.info('')
    def set_two_channel_audio(self):    self.log.info('')
    def stop(self):                     self.log.info('')


class CDPLayer(LogObject):
    def __init__(self, amplifier = None):
        super().__init__()
        self.amplifier = amplifier

    def on(self):       self.log.info('')
    def off(self):      self.log.info('')
    def eject(self):    self.log.info('')
    def pause(self):    self.log.info('')
    def play(self):     self.log.info('')
    def stop(self):     self.log.info('')


class Screen(LogObject):
    def up(self):       self.log.info('')
    def down(self):     self.log.info('')


class PopcornPopper(LogObject):
    def on(self):       self.log.info('')
    def off(self):      self.log.info('')
    def pop(self):      self.log.info('')

class TheaterLights(LogObject):
    def on(self):       self.log.info('')
    def off(self):      self.log.info('')
    def dim(self):      self.log.info('')


class Projector(LogObject):
    def __init__(self):
        super().__init__()
        self.dvdplayer = DVDPlayer()

    def on(self):               self.log.info('')
    def off(self):              self.log.info('')
    def tv_mode(self):          self.log.info('')
    def widescreen_mode(self):  self.log.info('')




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
            component = Tuner()
            component = DVDPlayer()
            component = CDPLayer()
            component = Amplifier()
            component = Screen()
            component = PopcornPopper()
            component = TheaterLights()
            component = Projector()
        

    def test_case_02(self):
        self.log.info('')          


# Run test suite
runner = unittest.TextTestRunner(stream=sys.stdout)
result = runner.run(unittest.makeSuite(Test))

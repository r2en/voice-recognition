This pages show you how to install library for using this application<br>
and show you error referrence.<br> 

First, you have to install SPTK(Signal processing Toolkit).<br>
SPTK has about 120 rich commands for analyzing speech.<br>
For example, FFT, MFCC, LPC etc in python.<br>


[Install SPTK](http://sp-tk.sourceforge.net/)


```ruby
$ Tar xvzf SPTK-3.10.tar.gz
$ cd SPTK-3.10
$ ./configure
$ make
$ sudo make install
```

If a compilation error appears, you have to install SPTK latest version.

```ruby
$ Impulse -h
```

If you success installation, the hepl messeage comes out.


```ruby
$ pip install pulp
$ pip install pyaudio
```

If a compilation error appears, you have to install portaudio.

```ruby
$ brew install portaudio
```

you may get an error it is not likned.
[warning portaudio already installed, it's just not linked]

and you type
```ruby
brew link port audio
```

```ruby
Error: Clould not symlikn include...
/user/local/.... is not writable
```

This problem can solve this command.

```ruby
sudo chown -R $USER /usr/local
```

Homebrew is when you install as arecommended user/local use.However you did the installer of portaudio with adoministrator pvivileges in /usr/local, Homebrew can't work as expected.







# Seans-Angular~~6~~7-Python-Flask-Boilerplate
Very basic Angular ~~6~~7 frontend with Python Flask RESTful API backend boiler plate

Updated to version 7

To Start

```bash
docker-compose up
```


This repository is used in a CI/CD video i created. 

[![CI/CD with Gitlab Runner and Docker-Compose](https://img.youtube.com/vi/RV0845KmsNI/0.jpg)](https://youtu.be/RV0845KmsNI)

Visit http://206.189.14.247:4200/ to see this app working.


## Note
Observation from ugrading from Angular 6 to Angular 7,
the `ng build process` now seems to require a much larger amount of memory for compiling just a basic app.
so now, in the dockerfile
rather than executing the command 

`RUN ng build --prod`,

I now need to manage how much ram is availbale for the process, and call the the `node` command instead, and add the `max_old_space_size` switch.

`RUN node --max_old_space_size=1024 node_modules/@angular/cli/bin/ng build --prod`

If the `max_old_space_size` switch still doesn't work for you, try adding a swap file to your VM.
This worked for me.
I added a 1GB swapfile to my VM.

See my swapfile tutorial at,

[![Create Swap File on Linux Ubuntu](https://img.youtube.com/vi/hXb50RxB-YU/0.jpg)](https://youtu.be/hXb50RxB-YU)

Read the videos description for all the commands entered during this video.






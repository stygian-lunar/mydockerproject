value = True
while value == True:
    import os
    os.system('clear')
    os.system('tput setaf 1')
    print('\t\t\tWELCOME TO DOCKER CONTROL')
    os.system('tput setaf 7')
    print('\t\t\t-------------------------')
    x = os.system('date +%D')
    print('Date:{}'.format(x))
    print('\n')
    print("Press 1 : For options\n",
          "Press 2 : For help\n",
          "Press 3 : To exit\n")
    print('Enter your choice:' , end = '')
    y = input()
    y = int(y)
    if y == 3:
        os.system('exit')
        value = False
    elif y == 2:
        os.system('tput setaf 3')
        print('Welcome to docker controller.\nThis application helps the users to use docker without remembering the actual commands')
        os.system('tput setaf 7')
    elif y == 1:
        active = True
        while active == True:
            os.system('clear')
            os.system('tput setaf 1')
            print('\t\t\tWELCOME TO DOCKER CONTROLLER')
            os.system('tput setaf 7')
            print('Date:' , end = '')
            os.system('date +%D')
            print('\t\t\t----------------------------')
            print('press 1 : to see the docker images\n'
            'press 2 : to see the containers running\n'
            'press 3 : to see the history of all the containers\n'
            'press 4 : to download new image\n'
            'press 5 : to launch new container in new terminal tab\n'
            'press 6 : to launch new container in the same terminal\n'
            'press 7 : to foreground a running container\n'
            'press 8 : to stop a runing container\n'
            'press 9 : to terminate a running container\n'
            'press 10 : to terminate all the running containers\n'
            'press 11 : to save any docker container as image\n'
            'press 12 : to delere any docker image\n'
            'press 13 : to run a single command in a container and to show the output\n'
            'press 14 : to run a single command in a container , show the output and then terminate the container\n'
            'press 15 : to get detailed information of running container'
            'press 16 : to show the ip address of the running container'
            'press 17 : to save the image as file in base os'
            'press 18 : to save the image as file and share it '
            'press q : to exit')
            print('enter your response:' , end = '')
            z = input()
            z = int(z)
            if z == 1:
                os.system('docker images')
            elif z == 2:
                os.system('docker ps')
            elif z == 3:
                os.system('docker ps -a')
            elif z == 4:
                print('enter the name and version of the image:')
                img_name = input('image name:')
                img_ver = input('image version:')
                os.system('pull {0}:{1}'.format(img_name,img_ver))
            elif z == 5:
                print('enter the tty of the terminal' , end='')
                tty = input('')
                opt = input('would you like to give some name to your os?(y,n)')
                if opt == 'n':
                    img_name = input('image name:')
                    img_ver = input('image version:')
                    os.system('docker run -it {0}:{1} > {2}'.format(img_name,img_ver,tty))
                elif opt == 'y':
                    os_name = input('os name:')
                    img_name = input('image name:')
                    img_ver = input('image version:')
                    os.system('docker run -it --name {0} {1}:{2} > {3}'.format(os_name,img_name,img_ver,tty))
            elif z == 6:
                print('enter the name and version of the image:')
                img_name = input('image name:')
                img_ver = input('image version:')
                os.system('docker -it {0}:{1}'.format(img_name,img_ver))
            elif z == 7:
                os.system('docker ps')
                print('enter the name of the container to be foregrounded:' , end = '')
                con_name = input()
                os.system('docker attach {}'.format(con_name)
            elif z == 8:
                os.system('docker ps')
                print('enter the name of the container to be stopped:' , end = '')
                con_name = input()
                os.system('docker stop {}'.format(con_name))
            elif z == 9:
                os.system('docker ps')
                print('enter the name of the container to be terminated:' , end = '')
                con_name = input()
                os.system('docker rm {}'.format(con_name))
            elif z == 10:
                os.system('docker rm $(docker ps -q)')
                os.system('docker ps -a')
            elif z == 11:
                os_name = input('enter the name of the container:')
                img_name = input('enter the name of new image:')
                ver = input('enter the version of the new image:')
                os.system('docker commit {0} {1}:{2}'.format(os_name,img_name,ver))
                os.system('docker images')
            elif z == 12:
                os_name = input('enter the name of the image:')
                ver = input('enter the version of  the image:')
                os.system('docker rmi -f {0}:{1}'.format(os_name,ver))
            elif z == 13:
                img_name = input('enter the name of container:')
                ver = input('enter the version of the container:')
                comm = input('enter the command you want to run:')
                os.system('docker run -it {0}:{1} {2}'.format(img_name,ver,comm))
            elif z == 14:
                img_name = input('enter the name of container:')
                ver = input('enter the version of the container:')
                comm = input('enter the command you want to run:')
                os.system('docker run -it --rm {0}:{1} {2}'.format(img_name,ver,comm))
            elif z == 15:
                os.system('docker ps') 
                img_name = input('enter the name of container:')
                os.system('docker inspect {}'.format(img_name))
            elif z == 16:
                os.system('docker ps')
                img_name = input('enter the name of container:')
                os.system('docker inspect --format "{{.Networkingsetting.IPAddress}}" {}'.format(img_name))
            elif z == 17:
                os.system('docker ps')
                name = input('enter the name of the container:')
                ver = input('enter the version:')
                file_name = input('enter the file name')
                os.system('docker save {0}:{1} -o {2}.tar'.format(name,ver,file_name))
            elif z == 18:
                os.system('docker ps')
                name = input('enter the name of the container:')
                ver = input('enter the version:')
                file_name = input('enter the file name')
                ip = input('enter target ip:')
                folder = input('enter target folder:')
                os.system('docker save {0}:{1} -o {2}.tar'.format(name,ver,file_name))
                os.system('scp /root/{} root@{}:/{}'.format(file_name,ip,folder))
                
            else:
                active = False
            input('press enter to continue....')
            os.system('clear')
    else:
        print('input not valid')
    input('press enter to continue......')
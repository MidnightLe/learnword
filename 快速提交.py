if __name__=='__main__':
    import os
    # git add .
    # git commit -m "beizhu "
    # git remote add origin https://github.com/MidnightLe/learnword.git
    # git push origin master
    os.system("git add .")
    commits=input("请输入备注信息:")
    os.system("git commit - m "+commits)
    a=os.popen("git remote")
    text=a.read()
    if text.find("origin")!=-1:
        print("远程库已经添加好了")
        os.system("git push origin master")
        
    else:
        oriname=input("请输入远程库地址:")
        os.system("git remote add origin "+oriname)
        os.system("git push -u origin master")

    a.close()
    print("-"*10+"任务完成"+"-"*10)
    os.system("pause")
# import sys
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
# sys.setrecursionlimit(0x100000)

#此代码会运行会报错“RecursionError: maximum recursion depth exceeded in comparison”。
#将1-4 行的取消注释，解决此问题，不得不说Python设置最大递归次数的方法十分怪异.
#如果只取消1,4行的注释，会遇到更加怪异的报错“Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)”

recur_count=0
def recur(max_recur=None):
    global recur_count
    recur_count+=1
    if recur_count<max_recur:
        recur(max_recur)

if __name__=="__main__":
    recur(20000)



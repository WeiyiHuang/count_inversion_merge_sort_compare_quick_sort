#merge 2 sorted arrays and count the inversions of the connected array
def merge_and_count(l,r):
    num_lr=[]
    c_merge=0
    i,j=0,0
    for k in range(0,len(l)+len(r)):
        if l[i]>r[j]:
            num_lr.append(r[j])
            c_merge+=len(l)-i
            j+=1
            if j==len(r):
                num_lr+=l[i:len(l)]
                break
        else:
            num_lr.append(l[i])
            i+=1
            if i==len(l):
                num_lr+=r[j:len(r)]
                break
    return num_lr,c_merge

#count the number of inversions of one disordered array based on the principle of merge sort
def count_inversion_merge_sort(num):
    '''devide the array into 2 halves, make recursive calls on the 2 arrays and calculate the number of inversions
    between 2 sorted array
    note that when array length decline to 1 or 0 the function returns'''
    n=0
    length=len(num)
    if length==0:
        return [],0
    else:
        if length==1:
            return num,n
        else:
            mid=(int)(length/2)
            num_l=num[0:mid]
            num_r=num[mid:length]
            num_l_sorted,n_l=count_inversion_merge_sort(num_l)
            num_r_sorted,n_r=count_inversion_merge_sort(num_r)
            num_sorted,n_merge=merge_and_count(num_l_sorted,num_r_sorted)
            n=n_l+n_r+n_merge
            return num_sorted,n

#throw the numbers which are smaller than pivot to the left, others to the right, and count the number of inversions
#vanished due to this operation
def throw(num):
    count=0
    l=[]
    r=[]
    pivot=num[0]
    num.reverse()
    for i in range(0,len(num)-1):
        if num[i]<pivot:
            l.append(num[i])
        else:
            r.append(num[i])
            count+=len(l)
    count+=len(l)
    num.reverse()
    l.reverse()
    r.reverse()
    return l,r,count

#count the number of inversions of one disordered array based on the principle of quick sort
def count_inversion_quick_sort(num):
    '''devide the array into 2 halves, make recursive calls on the 2 arrays and calculate the number of inversions
    vanished due to this operation
    note that when array length decline to 1 or 0 the function returns'''
    length=len(num)
    count=0
    if length<=1:
        return num,count
    else:
        l,r,count_throw=throw(num)
        num_l,count_l=count_inversion_quick_sort(l)
        num_r,count_r=count_inversion_quick_sort(r)
        count=count_l+count_r+count_throw
        return num_l+[num[0]]+num_r,count

def run_count_inversion_merge_sort():
    import string
    f=open('Q8.txt','r')
    number=f.read()
    f.close()
    number=number.split('\n')
    number=number[:100000]
    t=[]
    for n in number:
        t.append(string.atoi(n))
    number_sort,number_inversion=count_inversion_merge_sort(t)
    print 'Number of Inversions:'
    print number_inversion


def run_count_inversion_quick_sort():
    import string
    f=open('Q8.txt','r')
    number=f.read()
    f.close()
    number=number.split('\n')
    number=number[:100000]
    t=[]
    for n in number:
        t.append(string.atoi(n))
    number_sort,number_inversion=count_inversion_quick_sort(t)
    print 'Number of Inversions:'
    print number_inversion

if __name__=='__main__':
    from timeit import Timer
    t1=Timer("run_count_inversion_merge_sort()","from __main__ import run_count_inversion_merge_sort")
    turns=1
    print '###Array_Inversions_Sort_and_Count_Merge_Sort'
    t=t1.timeit(turns)/turns
    print 'Time:(run %d time(s))'%turns
    print t
    t2=Timer("run_count_inversion_quick_sort()","from __main__ import run_count_inversion_quick_sort")
    turns=1
    print '###Array_Inversions_Sort_and_Count_Quick_Sort'
    t=t2.timeit(turns)/turns
    print 'Time:(run %d time(s))'%turns
    print t

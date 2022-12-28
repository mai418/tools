#区切り文字でファイルを分割する(ファイル中に区切り文字が区切り以外に出てこないとする)

in_file_name = "/Users/yamada/kif11/actives_final.sdf"
out_file_name = "/Users/yamada/kif11/test_1.sdf" 


key = "$$$$" #区切り文字
count = 0 
sep = 50 #何個の区切り文字で別ファイルに分けるか
num = 1
max = 10

out_file = open(out_file_name, "w")
in_file = open(in_file_name)
line = in_file.readline()

while line:
    out_file.write(line)
    
    if key in line:
        count += 1
        
        if count == sep:
            num += 1
            count = 0
            out_file.close()
            out_file_name ="/Users/yamada/kif11/test_" + str(num) + ".sdf" #ファイル名と拡張子は随時設定
            
            if num > max:
                break
            out_file = open(out_file_name, "w")
    
    line = in_file.readline()

out_file.close()
in_file.close()
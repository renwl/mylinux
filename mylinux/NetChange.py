"""
this module can change the netlist's parameter
"""
import re
def ParCh(x,y,z):
	temp1=x + "=" +r"[-]?[+]?\d*[.]?\d*[e]?[-]?[+]?\d*[kmMGnupPfF]?"
	temp2=x + "=" + str(y)
	return re.sub(temp1,temp2,z)

def CorCh(x,z):
	#temp1="section=" + r"\w*[_]\w*"
	temp1=z.split("=")
	if re.search(r"[_]",temp1[-1]):
		temp2=temp1[-1].split("_")
		if re.search("snfp",x):
			return temp1[0] + "=" + temp2[0] + "_" + "tt\n"
		elif re.search("fnsp",x):
			return temp1[0] + "=" + temp2[0] + "_" + "tt\n"
		else:
			return temp1[0] + "=" + temp2[0] + "_" + x +"\n"
	else:
		return temp1[0] + "=" + x + "\n"

def LibCh(x):
	if re.search("ee",x):
		l=[r'include "/apps/Library/SMIC18/model/ASCII/e2r018_v1p8_spe.scs" section=tt',' \n',
		r'include "/apps/Library/SMIC18/model/ASCII/e2r018_v1p8_spe.scs" section=mim_tt',' \n',
		r'include "/apps/Library/SMIC18/model/ASCII/e2r018_v1p8_spe.scs" section=bjt_tt',' \n',
		r'include "/apps/Library/SMIC18/model/ASCII/e2r018_v1p8_spe.scs" section=res_tt','\n' ,
		r'include "/apps/Library/SMIC18/model/ASCII/e2r018_v1p8_spe.scs" section=pip_tt','\n' ]
		return l	
	elif re.search("95",x):
		l=[r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=bjt_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=dio_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=sdmte_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=res_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=mim_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=mom_tt','\n',
		r'include "/apps/Library/0p13/TD-SC95-KC-2002_V1/SPDK95HV_156072320_CDB_CDS_V0.6_0/smic95hv_156072320_1P5M_1TM_cdb_cds_V0.6_0/smic95/../models/spe/spocull_95hv_v0p6_spe.lib" section=pip_tt','\n']
		return l		
	else:
		return x

if __name__=="__main__":
	print "this is the main proc"
	ss=LibCh("smic18ee")
	print ss
	for i in ss:
		print CorCh("tt","ss",i)
		print CorCh("bjt_tt","bjt_ss",i)


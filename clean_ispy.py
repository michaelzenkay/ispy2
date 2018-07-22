import os
import sys
import glob
from os import rename
from os.path import join, dirname
sys.path.insert(0, '/data/mike/src/tools/')
import miketools as mt
import pydicom
#
# ## Convert to nii
# pats = mt.fdir('/data/mike/breast/ispy1/ISPY*')
# for pat in pats:                                                                    # Iterate through patients
#     dates = mt.fdir(join(pat,'*'))
#     for date in dates:
#         dsrc = date
#         studies = mt.fdir(join(date,'dyn*'))
#         for std in studies:                                                         # Iterate through studies
#             ssrc = std                                                              # Source is original folder
#             # Get info from first dicom
#             dcm = mt.fdir(join(std, '*.dcm'))                                       # Get dicoms in study
#             ds = pydicom.read_file(dcm[0])                                            # Read first dicom
#             # If dicoms have not yet been converted to nii - > convert
#             niis = mt.fdir(join(std, '*.nii.gz'))  # Get nii in folder
#             if len(niis) == 0:
#                 try:
#                     #os.system('dcm2nii -4 M -e N -p N -d N ' + dcm[0])
#                     os.system('dcm2nii -b /data/mike/src/ispy/dcm2niigui.ini ' + dcm[0])
#                 except:
#                     print('Dicom to Nii Conversion failed for ' + dcm[0])
#             try:
#                 dateID = ds.ClinicalTrialTimePointID                                # Get Study Time Point T1 T2 T3 T4
#                 ddes = join(dirname(date), dateID)
#             except:
#                 print('No Date ID information' + dcm[0])
#         try:
#             #rename(dsrc, ddes)  # Rename Dates to T1 T2 T3 T4 etc
#             print('skip date rename')
#         except:
#             print('Failed renaming date ' + dsrc)


#
# ### Sort
# pats = mt.fdir('/data/mike/breast/ispy1/ISPY*')
# for pat in pats:  # Iterate through patients
#     dates = mt.fdir(join(pat, '*'))
#     for date in dates:
#         try:
#             other = join(date, 'other')
#             os.mkdir(other)
#         except:
#             other = join(date, 'other')
#         dsrc = date
#         studies = mt.fdir(join(date, '*'))
#         t = 0
#         d = 0
#         for std in studies:  # Iterate through studies
#             ssrc = std  # Source is original folder
#             if os.path.basename(std)[0:2] != 'dy' and os.path.basename(std)[0:2] != 't2' and os.path.basename(std)[0:2] != 'ot' :
#                 # Get info from first dicom
#                 dcm = mt.fdir(join(std, '*.dcm'))  # Get dicoms in study
#                 ds = pydicom.read_file(dcm[0])  # Read first dicom
#                 ser = ds.SeriesDescription.lower()
#                 try:
#                     # # Find T2's and move (ser# < 5 digits)
#                     if len(str(ds.SeriesNumber))<5 and ds.SeriesDescription.lower().find("t2")>=0:
#                         t = t + 1
#                         sdes = join(dsrc, 't2_' + str(t) + os.path.basename(std))
#                     # Segmentations and ratios -> other_
#                     elif ser.find("_ser") >= 0 or ser.find("_pe1") >= 0 or ser.find("segmentation") >= 0 or ser.find("pjn") >= 0 or ser.find("average") >= 0 or ser.find("ax") >= 0 or ser.find("pjn") >= 0 or ser.find("fse") >= 0:
#                         sdes = join(other,os.path.basename(std))
#                     # Not dyns -> other
#                     elif ser.find("fiesta")>=0 and ser.find("test")>=0:
#                         sdes = join(other, os.path.basename(std))
#                     # Find dyns and move
#                     elif len(str(ds.SeriesNumber))<5 and ds.MRAcquisitionType=='3D':   #len(dcm)>90 and
#                         d = d + 1
#                         sdes = join(dsrc, 'dyn' + str(d) + '_' + os.path.basename(std))
#                     elif len(str(ds.SeriesNumber))<5 and ds[0x01171024].value[3][0x011710c0].value == 'SCORE':
#                         d = d + 1
#                         sdes = join(dsrc, 'dyn' + str(d) + '_' + os.path.basename(std))
#                     else:
#                         sdes = join(other, os.path.basename(std))
#                 except:
#                     sdes = join(other, os.path.basename(std))
#                 # Rename folders
#                 try:
#                     if sdes != ssrc:
#                         os.rename(ssrc,sdes)
#                         print('     Move from ' + ssrc + ' to ' + sdes + ' Successful')
#                 except:
#                     print('     Move from ' + ssrc + ' to ' + sdes + ' failed')
#         if len(glob.glob(join(date,'t2*')))>1:
#             a=[]
# #            print ('Found >1 t2 series in ' +date)
#         else:
#             a=[]
# #            print('No t2 series found in ' + date)
#         if len(glob.glob(join(date, 'dyn*'))) == 2:
#             a=[]
#             print('Found >1 dyn in ' + date)
#         else:
#             a = []
# #            print('No dyn found in ' + date)


#
# ## REVERSE - if you screw stuff up
#
# pats = mt.fdir('/data/mike/breast/ispy2/ISPY*')
# for pat in pats:  # Iterate through patients
#     dates = mt.fdir(join(pat, '*'))
#     for date in dates:
#         #os.mkdir(join(date),'other')
#         dsrc = date
#         studies = mt.fdir(join(date, '*'))
#         for std in studies:  # Iterate through studies
#             ssrc = std  # Source is original folder
#             # Get info from first dicom
#             dcm = mt.fdir(join(std, '*.dcm'))  # Get dicoms in study
#             try:
#                 ds = pydicom.read_file(dcm[0])  # Read first dicom
#                 sdes = join(dsrc, str(ds.SeriesNumber) + '-' + mt.joinalnu(ds.SeriesDescription.lower()))
#                 # Rename folders
#                 try:
#                     os.rename(ssrc,sdes)
#                 except:
#                     print('moving from ' + ssrc + ' to ' + sdes + ' failed')
#             except:
#                 print('dicom is being weird in folder '+std)

#
# ## clean up 4d volumes and stuff
# # Look for dyn folder
# # look for nii.gz
# # open with nib.load(filename).get_data
# import nibabel as nib
# fourd = 0
# threed = 0
# pats = mt.fdir('/data/mike/breast/ispy2/ISPY*')
# for pat in pats:  # Iterate through patients
#     dates = mt.fdir(join(pat, '*'))
#     for date in dates:
#         dynfolder= mt.fdir(join(date, 'dyn*'))
#         try:
#             nii = mt.fdir(join(dynfolder[0], '*.nii.gz'))   # Get nii.gz in study
#             niidata = nib.load(nii[0]).get_data()           # Read nii.gz
#             if len(niidata.shape)>3:                        # This is 4d nii - has either 3 or 2 dynamics
#                 for t in range(0,niidata.shape[3]):
#                     outfn = os.path.join(dynfolder[0],('dyn' + str(t) + '.nii.gz'))
#                     #print('4d' + outfn)
#             else:                                          # This is 3d nii - either has 1 or 2 other nii's
#                 t=0
#                 for n in range(0,len(nii)):
#                     niidata =nib.load(nii[n]).get_data()
#                     if len(niidata.shape)>3:
#                         for a in range(0,niidata.shape[3]):
#                             outfn = os.path.join(dynfolder[0], 'dyn' + str(t) + '.nii.gz')
#                             t=t+1
#                             #print('3d ' + str(outfn))
#                     else:
#                         outfn = os.path.join(dynfolder[0],('dyn' + str(t)+'.nii.gz'))
#                         t=t+1
#                         #print('3d ' + str(outfn))
#         except:
#             print('um ' + date + ' ' + str(len(dynfolder)))
#
#
# print('4d ' + str(fourd))
# print('3d ' + str(threed))

# from shutil import copyfile
# # Move dyn and t2 niis to date folder
# dyn = glob.glob('/data/mike/breast/ispy1/*/*/dyn*/*.nii*')
# t2 = glob.glob('/data/mike/breast/ispy1/*/*/t2*/*.nii*')
# for a in dyn:
#     copyfile(a,os.path.join(os.path.dirname(os.path.dirname(a)),'dyn' + os.path.basename(a)))
# for a in t2:
#     copyfile(a, os.path.join(os.path.dirname(os.path.dirname(a)), 't2' + os.path.basename(a)))


from shutil import copyfile
# Move dyn and t2 niis to date folder
pats = glob.glob('W:\\mike\\breast\\ispy\\1_sorted\\*')
for pat in pat:
    dyn = glob.glob(os.path.join(pat, T1, 'dyn*.nii.gz'))
    seg = glob.glob(os.path.join(pat, T1, 'seg.nii.gz'))
    if dyn.__len__()==0 and seg.__len__()==0:
        copyfile(a, os.path.join(os.path.dirname(os.path.dirname(a)), 'dyn' + os.path.basename(a)))
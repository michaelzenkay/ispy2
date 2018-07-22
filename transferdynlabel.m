pat = fdir('W:\mike\breast\ispy\1_sorted');
for i=1:length(pat)
    dyn = fdir(fullfile(pat(i).fname,'T1','dyn*.nii.gz'));
    seg = fdir(fullfile(pat(i).fname,'T1','seg*.nii.gz'));
    if length(seg)>0
        newpath = 'W:\mike\breast\ispy\2_labeledyn';
        for j=1:length(dyn)
            copyfile(dyn(j).fname,fullfile(newpath,[num2str(pat(i).name(end-2:end)) '_' num2str(j) '.nii.gz']))
        end
        copyfile(seg(1).fname,fullfile(newpath,[num2str(pat(i).name(end-2:end)) '_L.nii.gz']))
    end
end
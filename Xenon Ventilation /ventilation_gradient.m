%VENTILATION_GRADIENT Load patient ventilation and mask data and display
%statistics on relative concentration of ventilation in a line graph (14
%slices)
parent_dir = '/Users/kushgulati/Box/Patients/MatFiles/';
vent_ap_dir = '/Users/kushgulati/Box/Patients/ventilation_ap';
vent_ap_cor_dir = '/Users/kushgulati/Box/Patients/ventilation_ap_cor';
%figure_dir = '/Users/kushgulati/Box/Patients/Figures/';
mat = dir(fullfile(parent_dir, '*.mat'));
num_slices = 14;
plot_x = 1: num_slices;
percentile = 99;


for file = 1:2
    cd(parent_dir);
    load(mat(file).name);
    
    %Normalizes gas_highreso data
    gas_highreso = abs(gas_highreso).*mask_reg;
    gas_highreso = gas_highreso./prctile(gas_highreso(gas_highreso>0),percentile);
    gas_highreso(gas_highreso>1)=1;
    
    %Normalizes gas_highreso_cor data
    gas_highreso_cor = abs(gas_highreso_cor).*mask_reg;
    gas_highreso_cor = gas_highreso_cor./prctile(gas_highreso_cor(gas_highreso_cor>0),percentile);
    gas_highreso_cor(gas_highreso_cor>1)=1;
    
    
    
    %Calculates boundary_index for slices chosen and creates range of
    %ventilated slices
    [start, stop] = find_boundary_index3(mask_reg);
    while (mod(start, num_slices)~=0)
        start=start+1;
    end
    while(mod(stop, num_slices) ~=0)
        stop = stop-1;
    end
    
    %Establishes stepper to iterate through slices in the ventilated bounds
    %Initializes some array variables before loop iteration
    count = (stop - start)/num_slices;
    int_count = fix(count);
    
    ventilation_ap = [];
    average = [];
    total = [];
    
    ventilation_ap_cor = [];
    average_cor= [];
    total_cor = [];
    
    
    %Runs through "num_slices" slices in the ventilated boundaries
    %ventilation_ap and ventilation_ap_cor compile ventilation averages for each slice
    for x = start+int_count:int_count:stop
        slice = gas_highreso(:,:,x);
        total = size(slice(slice > 0));
        average = sum(slice, 'all') / total(1);
        ventilation_ap = [ventilation_ap, mean2(average)];
        
        slice_cor = gas_highreso_cor(:,:,x);
        total_cor = size(slice_cor(slice_cor > 0));
        average_cor = sum(slice_cor, 'all')/total_cor(1);
        ventilation_ap_cor= [ventilation_ap_cor, mean2(average_cor)];
    end
    
    %Uncomment if you want to see the plots
    figure
    hold on
    plot(plot_x,ventilation_ap, 'r--','LineWidth',3)
    plot(plot_x, ventilation_ap, 'r^', 'MarkerSize', 14, 'LineWidth', 3)
    plot(plot_x,ventilation_ap_cor, 'g--','LineWidth',3)
    plot(plot_x, ventilation_ap_cor, 'g^', 'MarkerSize', 14, 'LineWidth', 3)
    xlabel('Slice')
    ylabel('Normalized Ventilation')
    grid on
    title(strcat('Slice vs. Normalized Ventilation for Patient ',  mat(file).name))
    legend('Pre-Corrected Ventilation', 'Pre-Corrected Ventilation (data points)','Corrected Ventilation', 'Corrected Ventilation (data points)', 'Location', 'best')
    
    %Uncomment if you want to add to master list
%     master_ventilation_ap = [master_ventilation_ap, ventilation_ap];
%     master_ventilation_ap_cor = [master_ventilation_ap_cor, ventilation_ap_cor];
%     
    %Uncomment if you want to see the volumetric montage of the
    %gas_highreso and gas_highreso_cor
    %map = plasma(255); nslices = 14;
    %scaling = [.5 1.5]; vent_scaling = [0 1];
    %volume2montage(gas_highreso, map,[figure_dir,'show_vent.png'],...
    %'mask',mask,'scaling',vent_scaling,'nslices',nslices);
    %volume2montage(gas_highreso_cor, map,[figure_dir,'show_vent.png'],...
    %'mask',mask,'scaling',vent_scaling,'nslices',nslices);
    
    %Save Ventilation Data Files in New Folder
%     save(strcat('VentAp',mat(file).name), 'ventilation_ap');
%     cd(vent_ap_cor_dir);
%     save(strcat('VentApCor',mat(file).name), 'ventilation_ap_cor');
      disp(strcat('Completed and saved scan ' , mat(file).name));
end












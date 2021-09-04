import pandas as pd 
import statistics
import csv

df = pd.read_csv("data109.csv")

height_list=df["Height(Inches)"].to_list();
weight_list=df["Weight(Pounds)"].to_list();

height_mean=statistics.mean(height_list);
weight_mean=statistics.mean(weight_list);

height_median=statistics.median(height_list);
weight_median=statistics.median(weight_list);

height_mode=statistics.mode(height_list);
weight_mode=statistics.mode(weight_list);

print("mean,median and mode of height is {}, {} and {} respectively ".format(height_mean,height_median,height_mode))
print("mean,median and mode of weight is {}, {} and {} respectively ".format(weight_mean,weight_median,weight_mode))

height_stdev=statistics.stdev(height_list);
weight_stdev=statistics.stdev(weight_list);

height_first_stdev_start,height_first_stdev_end= height_mean-height_stdev,height_mean+height_stdev
height_second_stdev_start,height_second_stdev_end= height_mean-(2*height_stdev),height_mean+(2*height_stdev)
height_third_stdev_start,height_third_stdev_end= height_mean-(3*height_stdev),height_mean+(3*height_stdev)

weight_first_stdev_start,weight_first_stdev_end= weight_mean-weight_stdev,weight_mean+weight_stdev
weight_second_stdev_start,weight_second_stdev_end= weight_mean-(2*weight_stdev),weight_mean+(2*weight_stdev)
weight_third_stdev_start,weight_third_stdev_end= weight_mean-(3*weight_stdev),weight_mean+(3*weight_stdev)

height_list_of_data_within_1_stdev = [result for result in height_list if result > height_first_stdev_start and result < height_first_stdev_end]
height_list_of_data_within_2_stdev = [result for result in height_list if result > height_second_stdev_start and result < height_second_stdev_end]
height_list_of_data_within_3_stdev = [result for result in height_list if result > height_third_stdev_start and result < height_third_stdev_end]

weight_list_of_data_within_1_stdev = [result for result in weight_list if result > weight_first_stdev_start and result < weight_first_stdev_end]
weight_list_of_data_within_2_stdev = [result for result in weight_list if result > weight_second_stdev_start and result < weight_second_stdev_end]
weight_list_of_data_within_3_stdev = [result for result in weight_list if result > weight_third_stdev_start and result < weight_third_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_stdev)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_stdev)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_stdev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_stdev)*100.0/len(weight_list)))
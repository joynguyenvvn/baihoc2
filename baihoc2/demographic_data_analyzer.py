
import pandas as pd

def calculate_demographic_data(print_data=True):
    # Đọc dữ liệu từ file CSV
    df = pd.read_csv('adult.data.csv')

    # Số lượng người của mỗi chủng tộc
    race_count = df['race'].value_counts()

    # Độ tuổi trung bình của nam giới
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # Tỷ lệ người có bằng Cử nhân
    percentage_bachelors = ((df['education'] == 'Bachelors').mean() * 100).round(1)

    # Tỷ lệ phần trăm những người có trình độ học vấn cao kiếm được hơn 50 nghìn đô la
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = ((higher_education['salary'] == '>50K').mean() * 100).round(1)
    lower_education_rich = ((lower_education['salary'] == '>50K').mean() * 100).round(1)

    # Số giờ làm việc tối thiểu của một người mỗi tuần
    min_work_hours = df['hours-per-week'].min()

    # Tỷ lệ phần trăm những người làm việc tối thiểu số giờ mỗi tuần có mức lương trên 50 nghìn đô la
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = ((num_min_workers['salary'] == '>50K').mean() * 100).round(1)

    # Quốc gia nào có tỷ lệ người dân có thu nhập >50.000 đô la cao nhất và tỷ lệ đó là bao nhiêu
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = (country_salary / country_total * 100).max().round(1)

    # Xác định nghề nghiệp phổ biến nhất đối với những người có thu nhập >50.000 đô la ở Ấn Độ
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Số lượng người của mỗi chủng tộc:
", race_count)
        print("Độ tuổi trung bình của nam giới:", average_age_men)
        print(f"Tỷ lệ người có bằng Cử nhân: {percentage_bachelors}%")
        print(f"Tỷ lệ phần trăm những người có trình độ học vấn cao kiếm được hơn 50 nghìn đô la: {higher_education_rich}%")
        print(f"Tỷ lệ phần trăm những người không có trình độ học vấn cao kiếm được hơn 50 nghìn đô la: {lower_education_rich}%")
        print(f"Số giờ làm việc tối thiểu của một người mỗi tuần: {min_work_hours} giờ")
        print(f"Tỷ lệ phần trăm những người làm việc tối thiểu số giờ mỗi tuần có mức lương trên 50 nghìn đô la: {rich_percentage}%")
        print("Quốc gia có tỷ lệ người dân có thu nhập >50.000 đô la cao nhất:", highest_earning_country)
        print(f"Tỷ lệ đó là: {highest_earning_country_percentage}%")
        print("Nghề nghiệp phổ biến nhất đối với những người có thu nhập >50.000 đô la ở Ấn Độ:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

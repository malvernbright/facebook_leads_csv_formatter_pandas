import pandas as pd


def main():
    # Add file to workspace and input it's name without extension
    file = input("Enter csv file in your workspace (without extension): ")

    df = pd.read_csv(f'{file}.csv')

    df.head(3)  # Read first 3 lines of the file

    organization = input("Enter organization name you want to add to file: ")
    if len(organization) == 0:
        raise Exception(
            'OrganizationNotProvidedError: Organization Cannot be empty')
    else:
        df['Organization'] = organization
    output1 = input(
        "Enter output of the first file to be processed (don't include extension): ")
    df.to_csv(f'{output1}.csv', index=False)

    cols = pd.read_csv(f'{output1}.csv')

    unused_cols = ['ad_id', 'ad_name', 'adset_id',
                   'adset_name', 'campaign_id',
                   'campaign_name', 'form_name', 'is_organic', 'form_id']

    df2 = pd.read_csv(f'{output1}.csv', usecols=[
                      i for i in cols if i not in unused_cols])

    df3 = df2.rename(
        columns={
            'platform': 'Lead Source',
            'phone_number': 'Phone',
            'email': 'Email'})

    df3.loc[df3['Lead Source'] == 'fb', 'Lead Source'] = 'Facebook'
    df3.loc[df3['Lead Source'] == 'ig', 'Lead Source'] = 'Instagram'
    company = input("Enter company name: ")
    df3['Company'] = company if company != '' else 'No Company'

    df3[['First Name', 'Last Name']] = df3['full_name'].str.split(
        ' ', 1, expand=True)

    final_file = input('Enter final file name: ')
    if len(final_file) == 0:
        raise Exception(
            'EmptyFileNameError: cannot save file with an empty name!')
    else:
        df3.drop(
            columns=['full_name', 'created_time']
        ).to_csv(
            f'{final_file}.csv', encoding='utf-8', index=False
        )

    df5 = pd.read_csv(f'{final_file}.csv')

    df5


if __name__ == 'main':
    main()

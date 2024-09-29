import requests
import pandas as pd
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


if __name__ == '__main__':

    URL="https://www.bmltadmin.anonimowinarkomani.org/main_server/client_interface/csv/?switcher=GetSearchResults&services=8&data_field_key=weekday_tinyint,start_time,duration_time,meeting_name,location_text,location_info,location_street,location_city_subsection,location_municipality"
    content = requests.get(URL).content.decode()
    data_table = list(csv.reader(content.splitlines(),delimiter=','))
    df = pd.DataFrame(data_table)
    header = df.iloc[0]
    df = df[1:]
    df.columns = header
    cols = set(df.columns)
    #cols.remove('location_info')
    #cols.remove('location_city_subsection')
    cols = list(cols)
    df2 = df[cols]
    print(df)
    
    fig, ax =plt.subplots(figsize=(20,11))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=df2.values,colLabels=df2.columns,loc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(8)
    the_table.auto_set_column_width(col=list(range(len(df2.columns))))

    pp = PdfPages("lista_mityngow_okreg_warszawski.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()

# 🍄 Mushroom Vision 🍄

A simple dashboard visualizing the total dataset with rolling-average trends (using https://plotly.com/).

To run me, first clone and enter:
* `git clone https://github.com/Jack-Naughton/mushroom_cup.git; cd mushroom_cup`

Then execute the provided helper shell script
* `source mushroom_time.sh`

Finally, navigate home and view the 3 dashboards
* `http://localhost:8000/`


## Installed Requirements
* django
* pandas
* plotly

## Notes
Each dashboard shows all 10,000 data points per dataset.

Outliers ( > 3 standard deviations) are shown in red.

Plotly behavior allows for zooming / panning via click-and-drag.

Thank you for the opportunity!

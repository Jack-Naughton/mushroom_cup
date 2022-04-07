# 🍄 Mushroom Vision 🍄

A simple dashboard visualizing the total dataset with rolling-average trends (using https://plotly.com/).

This project relies on docker. If you don't have it installed or run into issues, you can view it at https://jacknaughton.com/mushroom_cup (I will remove this once the application process if done)

To run me, first clone and enter:
* `git clone https://github.com/Jack-Naughton/mushroom_cup.git; cd mushroom_cup`

Then spin it up with docker (may take a few minutes the first time)
* `docker compose up`

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

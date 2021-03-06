library(tidyverse)
library(gganimate)
library(gapminder)
theme_set(theme_classic())
library(rJava)
library(xlsx)
covid <- read.xlsx('c:/covid19.xlsx', sheetIndex = 1, encoding = 'utf-8')
covid

gap <- covid %>%
  group_by(year) %>%
  # The * 1 makes it possible to have non-integer ranks while sliding
  mutate(rank = min_rank(-value) * 1,
         Value_rel = value/value[rank==1],
         Value_lbl = paste0(" ",value)) %>%
  filter(rank <=13) %>%
  ungroup()

p <- ggplot(gap, aes(rank, group = country, 
                     fill = as.factor(country), color = as.factor(country))) +
  geom_tile(aes(y = value/2,
                height = value,
                width = 0.9), alpha = 0.8, color = NA) +
  geom_text(aes(y = 0, label = paste(country, " ")), vjust = 0.2, hjust = 1) +
  geom_text(aes(y=value,label = Value_lbl, hjust=0)) +
  coord_flip(clip = "off", expand = FALSE) +
  scale_y_continuous(labels = scales::comma) +
  scale_x_reverse() +
  guides(color = FALSE, fill = FALSE) +
  
  labs(title='{closest_state}', x = "", y = "Covid19 Number",
       caption = "Sources: Covid19 | Plot generated by Team4") +
  theme(plot.title = element_text(hjust = 0, size = 22),
        axis.ticks.y = element_blank(),  # These relate to the axes post-flip
        axis.text.y  = element_blank(),  # These relate to the axes post-flip
        plot.margin = margin(1,1,1,4, "cm")) +
  
  transition_states(year, transition_length = 4, state_length = 1) +
  ease_aes('cubic-in-out')

animate(p, 200, fps = 7, duration = 40, width = 800, height = 600, renderer = gifski_renderer("Ȯ���ڼ�.gif"))
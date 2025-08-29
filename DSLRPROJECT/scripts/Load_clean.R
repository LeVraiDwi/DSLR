# scripts/load_clean.R

load_and_clean <- function(file_path) {
  data <- read.csv(file_path)        # load the dataset
  return(data)
}
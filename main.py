import pyshorteners

link = 'https://ttdownloader.com/dl.php?v=YTo0OntzOjk6IndhdGVybWFyayI7YjowO3M6NzoidmlkZW9JZCI7czozMjoiN2QzNjUxYjNkODFkY2E2YTBiMjQ5YWE0ODdhZjk1YWEiO3M6MzoidWlkIjtzOjMyOiI1YmZlNTJjYmZkNGI3YzQ0NWYzZTBlMGI2YTY1M2M5YyI7czo0OiJ0aW1lIjtpOjE2MjUyNTc5NjQ7fQ=='

short = pyshorteners.Shortener()

x = short.tinyurl.short(link)

print(x)
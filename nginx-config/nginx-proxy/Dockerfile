# checkov:skip=CKV_DOCKER_2
# checkov:skip=CKV_DOCKER_3
# checkov:skip=CKV_DOCKER_7

FROM nginx:latest

# Copy nginx configuration from nginx-proxy directory
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
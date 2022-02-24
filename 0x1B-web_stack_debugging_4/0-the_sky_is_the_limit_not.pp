# Simulate 2000 HTTP requests to a web server

exec { 'Modify limit':
    command  => 'sed -i "s/-n 15/ -n 30000/g" /etc/default/nginx',
    provider => 'shell'
}

exec { 'Restart nginx':
    command  => 'service nginx restart',
    provider => 'shell'
}

FROM php:7.4-apache

RUN apt-get update && apt-get install -y git zip unzip libzip-dev

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN docker-php-ext-install zip

COPY composer.lock /var/www/html/
COPY composer.json /var/www/html/

RUN composer install --no-dev --prefer-dist

COPY . /var/www/html/

WORKDIR /var/www/html

EXPOSE 80
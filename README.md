# Shutterfly Sites API

I wanted to download all the photos from a Shutterfly Share Site, but neither the web or the native mobile app seemed particularly great. Sadly Shutterfly doesn't expose a public API, so I reverse engineered it to download all the photos.

It depends on grabbing the authentication token from the cookie once you are logged in to the website (as I didn't bother to implement the login also).

## Usage

To download all photos in all albums:

    > shutterfly_sites_api/api.py --site SITE --token TOKEN --directory DIRECTORY

* `site` - name of the Share Sites (ie the first part of the domain name, ie <https://SITE.shutterfly.com>
* `token` - contents of the `ShrAuth` cookie
* `directory` - where to download the photos to

## API Notes

As mentioned, Shutterfly doesn't actually have a public API, so I had to deduce it from their website. It's fairly simple though. All the data is exposed through <https://cmd.shutterfly.com/commands/format/js>. All the picture information can be fetched through `?site=SITE&page=SITE%2fpictures&v=1&usejwt_token=true`. Each album can be found inside `Shr.P.sections[0].groups` and the photo information is inside `.items` in each group.

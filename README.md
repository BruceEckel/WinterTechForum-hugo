# The Winter Tech Forum Hugo Static Site Source

Hugo Static Site for the [Winter Tech Forum Conference](www.WinterTechForum.com).

Because of the theme, the site automatically works well on phones as well as
computers and tablets.

Everything is in markdown so it's very easy to add/edit content. If you look
at the "content" subdirectory you'll see how straightforward it is to add new
pages.

I think this will also make it easier to clone/set up new conferences.

I'm still coming up the curve on static site generators in general and Hugo in
particular so if anyone knows more please feel free to make suggestions and/or
pull requests.

## To Build:

1.  [Install the Hugo](https://hugodocs.info/getting-started/installing/#quick-install) static site generator.

2.  Clone this repository into your "git" subdirectory.

3.  From within this repository, run `hugo server` and open your browser at the URL given.

4.  To create the deployable version, run `hugo` from within this repository.
    You should now see a `public` directory, which contains the deployable file
    set.

5.  To duplicate what happens during an actual deploy, first clone
    [WinterTechForum.github.io](https://github.com/WinterTechForum/WinterTechForum.github.io)
    into your "git" subdirectory. Now run `python deploy.py` from within this
    subdirectory.

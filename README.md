# The Winter Tech Forum Hugo Static Site Source

Hugo Static Site for the [Winter Tech Forum Conference](https://www.WinterTechForum.com).

Because of the theme, the site automatically works well on phones as well as
computers and tablets.

Everything is in markdown to make it easy to add/edit content. If you look
at the "content" subdirectory you'll see how to add new pages.

This should also make it easier to clone/set up new conferences.

## Requirements

- Git
- [Hugo](https://gohugo.io/getting-started/installing/) `v0.59.0`
- Python (only for deploy)

## Setup

```bash
git clone git@github.com:BruceEckel/WinterTechForum-hugo.git
cd WinterTechForum-hugo
git clone git@github.com:pavelbinar/hugo-material-banner.git themes/hugo-material-banner
```

## Development

```bash
hugo server
```

## Build

```bash
hugo server
```

The build output will be in the `public` folder.

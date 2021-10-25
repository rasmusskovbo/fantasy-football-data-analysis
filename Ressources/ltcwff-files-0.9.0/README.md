# README
These are the files for the book [Learn to Code with Fantasy
Football](https://fantasycoding.com).

If you're not familiar with Git or GitHub, no problem. Just click the `Source
code` link under the latest release to download the files.  This will download
a file called `ltcwff-files-vX.X.X.zip`, where X.X.X is the latest version.

When you unzip these (note in the book I've dropped the version number and
renamed the directory just `ltcwff-files`, which you can do too) you'll see
four sub-directories: `code`, `data`, `anki`, `solutions-to-excercises`.

You don't have to do anything with these right now except know where you put
them. For example, on my mac, I have them in my home directory:

`/Users/nathanbraun/ltcwff-files`

If I were using Windows, it might look like this:

`C:\Users\nathanbraun\ltcwff-files`

Set these aside for now and we'll pick them up in chapter 2.

## Changelog
### v0.9.0 (2021-06-16)
Updated visualization section + associated homework problems to use Seaborn
0.11.x (September 2020), which added a new `displot` function. This means
making our distribution plots change from, say:

```python
g = (sns.FacetGrid(df)
     .map(sns.kdeplot, 'std', shade=True))
```

To:

```python
g = sns.displot(df, x='std', kind='kde', fill=True)
```

It also opens up some new possibilities (e.g. with plotting empirical CDFs)
that I might discuss in a future update.

### v0.8.0
Add this changelog, bundle files in an github release vs including with SendOwl.

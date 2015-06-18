"""Extensible JSON/YAML/RAML/... data loader."""

__all__ = 'Loader'.split()
__version__ = '0.1.3'

from os.path import splitext, dirname

class Loader(object):
    markups = dict(
        json = 'json',
        yaml = 'yaml',
        yml  = 'yaml',
        raml = 'raml',
        )
    default_markup = 'yaml'

    log = None
    name = 'data'

    def __init__(self, name=None, default_markup=None, **options):
        if name is not None:
            self.name = name
        if default_markup is not None:
            self.default_markup = default_markup
        if options:
            self.__dict__.update(options)

    def load(self, f, markup=None, name=None, **options):
        path = f if isinstance(f, basestring) else f.name
        if markup is None:
            markup = self.markups.get(splitext(path)[-1][1:], self.default_markup)
        if self.log:
            self.log.info('get %s: %s [%s]', name or self.name, path, markup)
        return self.postprocess(getattr(self, 'load_{0}'.format(markup))(f), name, **options)

    __call__ = load

    def postprocess(self, data, name=None, path=None):
        if self.log:
            self.log.info('got %s: %s%s', name or self.name, type(data).__name__,
                ' [%d]' % len(data) if hasattr(data, '__len__') else '')
        return data

    def load_raml(self, f):
        if isinstance(f, basestring):
            from pyraml.parser import load
            return load(f)
        else:
            from pyraml.parser import parse
            return parse(f.read(), dirname(f.name))

    def load_yaml(self, f):
        from yaml import load
        if isinstance(f, basestring):
            with file(f, 'r') as fp:
                return load(fp)
        else:
            return load(f)

    def load_json(self, f):
        from json import load
        if isinstance(f, basestring):
            with file(f, 'r') as fp:
                return load(fp)
        else:
            return load(f)

    def __str__(self):
        return '{0}.{1}({2}: *{3}, {4})'.format(self.__class__.__module__, self.__class__.__name__.lower(),
            self.name, self.default_markup,
            ', '.join(k for k in sorted(set(self.markups.values())) if k != self.default_markup))

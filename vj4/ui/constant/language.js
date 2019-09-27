import attachObjectMeta from './util/objectMeta';

export const LANG_TEXTS = {
  other: 'Other',
  c: 'C',
  cc: 'C++',
  'llvm-c': 'C (Clang, with memory check)',
  'llvm-cc': 'C++ (Clang++, with memory check)',
  cmake: 'CMake',
  make: 'GNU Make',
  matlab: 'MATLAB',
  cs: 'C#',
  pas: 'Pascal',
  java: 'Java',
  py: 'Python',
  py3: 'Python 3',
  octave: 'Octave',
  php: 'PHP',
  rs: 'Rust',
  hs: 'Haskell',
  js: 'JavaScript',
  go: 'Go',
  rb: 'Ruby',
};

export const LANG_HIGHLIGHT_ID = {
  other: 'other',
  c: 'c',
  cc: 'cpp',
  'llvm-c': 'c',
  'llvm-cc': 'cpp',
  cmake: 'cmake',
  make: 'make',
  matlab: 'matlab',
  cs: 'csharp',
  pas: 'pascal',
  java: 'java',
  py: 'python',
  py3: 'python',
  octave: 'octave',
  php: 'php',
  rs: 'rust',
  hs: 'haskell',
  js: 'javascript',
  go: 'go',
  rb: 'ruby',
};

export const LANG_CODEMIRROR_MODES = {
  other: 'text/x-sh',
  c: 'text/x-csrc',
  cc: 'text/x-c++src',
  'llvm-c': 'text/x-csrc',
  'llvm-cc': 'text/x-c++src',
  cmake: 'text/x-cmake',
  make: 'text/x-sh',
  matlab: 'text/x-octave',
  cs: 'text/x-csharp',
  pas: 'text/x-pascal',
  java: 'text/x-java',
  py: 'text/x-python',
  py3: 'text/x-python',
  octave: 'text/x-octave',
  php: 'text/x-php',
  rs: 'text/x-rustsrc',
  hs: 'text/x-haskell',
  js: 'text/javascript',
  go: 'text/x-go',
  rb: 'text/x-ruby',
};
attachObjectMeta(LANG_CODEMIRROR_MODES, 'exportToPython', false);

export const LANG_MOSS = {
  c: 'c',
  cc: 'cc',
  java: 'java',
  ml: 'ml',
  pascal: 'pascal',
  ada: 'ada',
  lisp: 'lisp',
  scheme: 'scheme',
  haskell: 'haskell',
  fortran: 'fortran',
  ascii: 'ascii',
  vhdl: 'vhdl',
  perl: 'perl',
  matlab: 'matlab',
  python: 'python',
  mips: 'mips',
  prolog: 'prolog',
  spice: 'spice',
  vb: 'vb',
  csharp: 'csharp',
  modula2: 'modula2',
  a8086: 'a8086',
  javascript: 'javascript',
  plsql: 'plsql',
};

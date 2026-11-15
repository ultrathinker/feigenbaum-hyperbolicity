# -*- coding: utf-8 -*-
"""Манифест пакета: SHA-256 всех файлов.

    python _manifest.py            — ПЕРЕСЧИТАТЬ манифест (перезаписывает файл)
    python _manifest.py verify     — ПРОВЕРИТЬ пакет против манифеста

Раньше здесь был только режим записи, и `MANIFEST.sha256` описывался
в README как «хеши всех файлов пакета» без указания, чем их сверять. При
внешней проверке скрипт запускали, видели «файлов 918, 18.7 МБ» и писали
«manifest verified, no mismatches» — хотя запуск не сверял ничего, а молча
переписывал манифест под то, что лежит на диске. Проверка, которая не может
провалиться, — не проверка; `verify` возвращает ненулевой код возврата при
любом расхождении: изменённый файл, лишний файл, недостающий файл.

Сам `_manifest.py` раньше исключал себя из манифеста — значит
подмена верификатора была невидима для его же проверки. Теперь он в манифесте;
вне манифеста только `MANIFEST.sha256` (по построению) и `СОСТОЯНИЕ.md`.
"""
import os
import sys
import hashlib
import time

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, 'MANIFEST.sha256')
SKIP = ('MANIFEST.sha256', 'СОСТОЯНИЕ.md')   # сам верификатор — в манифесте
# Windows не различает регистр имён файлов, а Python-сравнение —
# различает: реально переименованный (только регистром) файл тихо
# перестал бы исключаться и молча попал бы в манифест как обычный.
SKIP_LOWER = {s.lower() for s in SKIP}
sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def scan():
    """(словарь путь -> sha256, суммарный объём) по тем же правилам, что и запись."""
    rows, total = {}, 0
    for root, dirs, files in os.walk(HERE):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for f in sorted(files):
            if f in SKIP or f.lower() in SKIP_LOWER:
                continue
            p = os.path.join(root, f)
            h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
            rel = os.path.relpath(p, HERE).replace(os.sep, '/')
            rows[rel] = h
            total += os.path.getsize(p)
    return rows, total


def write():
    rows, total = scan()
    lines = ['%s  %s' % (rows[r], r) for r in sorted(rows)]
    # только LF — иначе `sha256sum -c MANIFEST.sha256` на Linux/macOS
    # не находит ни одного файла ('путь\r').
    open(MANIFEST, 'w', encoding='utf-8', newline='\n').write(
        '# %s  файлов: %d  объём: %.1f МБ\n'
        % (time.strftime('%Y-%m-%d %H:%M'), len(lines), total / 2 ** 20)
        + '\n'.join(lines) + '\n')
    print('манифест записан: файлов %d, %.1f МБ' % (len(lines), total / 2 ** 20))
    return 0


def verify():
    if not os.path.exists(MANIFEST):
        print('*** ПРОВАЛ: MANIFEST.sha256 отсутствует')
        return 2
    want = {}
    for line in open(MANIFEST, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        h, _, rel = line.partition('  ')
        want[rel] = h
    have, total = scan()

    changed = sorted(r for r in set(want) & set(have) if want[r] != have[r])
    missing = sorted(set(want) - set(have))
    extra = sorted(set(have) - set(want))

    for r in changed:
        print('*** ИЗМЕНЁН   %s' % r)
    for r in missing:
        print('*** ПРОПАЛ    %s' % r)
    for r in extra:
        print('*** ЛИШНИЙ    %s' % r)

    bad = len(changed) + len(missing) + len(extra)
    print('сверено с манифестом: %d файлов, %.1f МБ; '
          'изменено %d, пропало %d, лишних %d'
          % (len(have), total / 2 ** 20, len(changed), len(missing), len(extra)))
    if bad:
        print('ИТОГ: ПАКЕТ НЕ СООТВЕТСТВУЕТ МАНИФЕСТУ (%d расхождений)' % bad)
        return 1
    print('ИТОГ: пакет соответствует манифесту')
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'write'
    if mode == 'verify':
        sys.exit(verify())
    if mode in ('write', 'generate'):
        sys.exit(write())
    print('использование: python _manifest.py [write|verify]')
    sys.exit(2)

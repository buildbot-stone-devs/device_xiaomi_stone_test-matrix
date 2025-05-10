#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/stone',
    'hardware/qcom-caf/sm8350',
    'hardware/xiaomi',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/bin/STFlashTool': blob_fixup()
         .add_needed('libbase_shim.so'),
    'vendor/lib64/camera/components/com.qti.node.mialgocontrol.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
     'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed(
            'libcrypto.so',
            'libcrypto-v33.so'
       ),
       'vendor/etc/seccomp_policy/imsrtp.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    ('vendor/lib64/libalLDC.so','vendor/lib64/libalhLDC.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
}

module = ExtractUtilsModule(
    'stone',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

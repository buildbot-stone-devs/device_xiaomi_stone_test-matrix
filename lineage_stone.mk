#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

# Inherit from stone device
$(call inherit-product, device/xiaomi/stone/device.mk)

PREBUILT_KERNEL := true

PRODUCT_NAME := lineage_stone
PRODUCT_DEVICE := stone
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi

# Matrixx
MATRIXX_BUILD_TYPE := Official
MATRIXX_MAINTAINER := Mayuresh & Khnome
MATRIXX_CHIPSET := SM6375
MATRIXX_BATTERY := 5000mah
MATRIXX_DISPLAY := 1080x2400

# To include Gapps 
WITH_GMS := true

# To Build Google(Dailer, Message, Phone) and BCR
WITH_GMS_COMMS_SUITE := true

BuildFingerprint=POCO/moonstone_p_global/moonstone:14/UKQ1.231003.002/V816.0.14.0.UMPMIXM:user/release-keys

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

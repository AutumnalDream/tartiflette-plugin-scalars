import pytest

from tartiflette_plugin_scalars import _generate_scalars


@pytest.mark.parametrize(
    "schema_name,config,scalars",
    [
        (
            "empty_conf",
            {},
            [
                "scalar EmailAddress",
                "scalar NaiveDateTime",
                "scalar DateTime",
                "scalar Duration",
                "scalar NegativeFloat",
                "scalar NegativeInt",
                "scalar NonNegativeFloat",
                "scalar NonNegativeInt",
                "scalar NonPositiveFloat",
                "scalar NonPositiveInt",
                "scalar PositiveFloat",
                "scalar PositiveInt",
                "scalar Long",
                "scalar BigInt",
                "scalar UnsignedInt",
                "scalar PhoneNumber",
                "scalar PostalCode",
                "scalar URL",
                "scalar GUID",
                "scalar HexColorCode",
                "scalar HSL",
                "scalar HSLA",
                "scalar RGB",
                "scalar RGBA",
                "scalar IPv4",
                "scalar IPv6",
                "scalar ISBN",
                "scalar MAC",
                "scalar Port",
                "scalar USCurrency",
                "scalar JSON",
                "scalar JSONObject",
                "scalar GeoJSON",
            ],
        ),
        (
            "disable_all",
            {
                "email_address": {"enabled": False},
                "datetime": {"enabled": False},
                "naive_datetime": {"enabled": False},
                "duration": {"enabled": False},
                "negative_float": {"enabled": False},
                "negative_int": {"enabled": False},
                "non_negative_float": {"enabled": False},
                "non_negative_int": {"enabled": False},
                "non_positive_float": {"enabled": False},
                "non_positive_int": {"enabled": False},
                "positive_float": {"enabled": False},
                "positive_int": {"enabled": False},
                "long": {"enabled": False},
                "big_int": {"enabled": False},
                "unsigned_int": {"enabled": False},
                "phone_number": {"enabled": False},
                "postal_code": {"enabled": False},
                "url": {"enabled": False},
                "guid": {"enabled": False},
                "hex_color_code": {"enabled": False},
                "hsl": {"enabled": False},
                "hsla": {"enabled": False},
                "rgb": {"enabled": False},
                "rgba": {"enabled": False},
                "ipv4": {"enabled": False},
                "ipv6": {"enabled": False},
                "isbn": {"enabled": False},
                "mac": {"enabled": False},
                "port": {"enabled": False},
                "us_currency": {"enabled": False},
                "json": {"enabled": False},
                "json_object": {"enabled": False},
                "geo_json": {"enabled": False},
            },
            [],
        ),
        (
            "enable_all",
            {
                "email_address": {"enabled": True},
                "datetime": {"enabled": True},
                "naive_datetime": {"enabled": True},
                "duration": {"enabled": True},
                "negative_float": {"enabled": True},
                "negative_int": {"enabled": True},
                "non_negative_float": {"enabled": True},
                "non_negative_int": {"enabled": True},
                "non_positive_float": {"enabled": True},
                "non_positive_int": {"enabled": True},
                "positive_float": {"enabled": True},
                "positive_int": {"enabled": True},
                "long": {"enabled": True},
                "big_int": {"enabled": True},
                "unsigned_int": {"enabled": True},
                "phone_number": {"enabled": True},
                "url": {"enabled": True},
                "guid": {"enabled": True},
                "hex_color_code": {"enabled": True},
                "hsl": {"enabled": True},
                "hsla": {"enabled": True},
                "rgb": {"enabled": True},
                "rgba": {"enabled": True},
                "ipv4": {"enabled": True},
                "ipv6": {"enabled": True},
                "isbn": {"enabled": True},
                "mac": {"enabled": True},
                "port": {"enabled": True},
                "us_currency": {"enabled": True},
                "json": {"enabled": True},
                "json_object": {"enabled": True},
                "geo_json": {"enabled": True},
            },
            [
                "scalar EmailAddress",
                "scalar NaiveDateTime",
                "scalar DateTime",
                "scalar Duration",
                "scalar NegativeFloat",
                "scalar NegativeInt",
                "scalar NonNegativeFloat",
                "scalar NonNegativeInt",
                "scalar NonPositiveFloat",
                "scalar NonPositiveInt",
                "scalar PositiveFloat",
                "scalar PositiveInt",
                "scalar Long",
                "scalar BigInt",
                "scalar UnsignedInt",
                "scalar PhoneNumber",
                "scalar PostalCode",
                "scalar URL",
                "scalar GUID",
                "scalar HexColorCode",
                "scalar HSL",
                "scalar HSLA",
                "scalar RGB",
                "scalar RGBA",
                "scalar IPv4",
                "scalar IPv6",
                "scalar ISBN",
                "scalar MAC",
                "scalar Port",
                "scalar USCurrency",
                "scalar JSON",
                "scalar JSONObject",
                "scalar GeoJSON",
            ],
        ),
        (
            "rename_all",
            {
                "email_address": {"name": "MyEmailAddress"},
                "naive_datetime": {"name": "MyNaiveDateTime"},
                "datetime": {"name": "MyDateTime"},
                "duration": {"name": "MyDuration"},
                "negative_float": {"name": "MyNegativeFloat"},
                "negative_int": {"name": "MyNegativeInt"},
                "non_negative_float": {"name": "MyNonNegativeFloat"},
                "non_negative_int": {"name": "MyNonNegativeInt"},
                "non_positive_float": {"name": "MyNonPositiveFloat"},
                "non_positive_int": {"name": "MyNonPositiveInt"},
                "positive_float": {"name": "MyPositiveFloat"},
                "positive_int": {"name": "MyPositiveInt"},
                "long": {"name": "MyLong"},
                "big_int": {"name": "MyBigInt"},
                "unsigned_int": {"name": "MyUnsignedInt"},
                "phone_number": {"name": "MyPhoneNumber"},
                "postal_code": {"name": "MyPostalCode"},
                "url": {"name": "MyURL"},
                "guid": {"name": "MyGUID"},
                "hex_color_code": {"name": "MyHexColorCode"},
                "hsl": {"name": "MyHSL"},
                "hsla": {"name": "MyHSLA"},
                "rgb": {"name": "MyRGB"},
                "rgba": {"name": "MyRGBA"},
                "ipv4": {"name": "MyIPv4"},
                "ipv6": {"name": "MyIPv6"},
                "isbn": {"name": "MyISBN"},
                "mac": {"name": "MyMAC"},
                "port": {"name": "MyPort"},
                "us_currency": {"name": "MyUSCurrency"},
                "json": {"name": "MyJSON"},
                "json_object": {"name": "MyJSONObject"},
                "geo_json": {"name": "MyGeoJSON"},
            },
            [
                "scalar MyEmailAddress",
                "scalar MyNaiveDateTime",
                "scalar MyDateTime",
                "scalar MyDuration",
                "scalar MyNegativeFloat",
                "scalar MyNegativeInt",
                "scalar MyNonNegativeFloat",
                "scalar MyNonNegativeInt",
                "scalar MyNonPositiveFloat",
                "scalar MyNonPositiveInt",
                "scalar MyPositiveFloat",
                "scalar MyPositiveInt",
                "scalar MyLong",
                "scalar MyBigInt",
                "scalar MyUnsignedInt",
                "scalar MyPhoneNumber",
                "scalar MyPostalCode",
                "scalar MyURL",
                "scalar MyGUID",
                "scalar MyHexColorCode",
                "scalar MyHSL",
                "scalar MyHSLA",
                "scalar MyRGB",
                "scalar MyRGBA",
                "scalar MyIPv4",
                "scalar MyIPv6",
                "scalar MyISBN",
                "scalar MyMAC",
                "scalar MyPort",
                "scalar MyUSCurrency",
                "scalar MyJSON",
                "scalar MyJSONObject",
                "scalar MyGeoJSON",
            ],
        ),
    ],
)
def test_generate_scalars(schema_name, config, scalars):
    assert sorted(_generate_scalars(schema_name, config)) == sorted(scalars)

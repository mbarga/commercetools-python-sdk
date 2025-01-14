# DO NOT EDIT! This file is automatically generated

import marshmallow
import marshmallow_enum

from commercetools import helpers, types

__all__ = [
    "CartClassificationTypeSchema",
    "CartScoreTypeSchema",
    "CartValueTypeSchema",
    "ExternalOAuthSchema",
    "ProjectChangeCountriesActionSchema",
    "ProjectChangeCurrenciesActionSchema",
    "ProjectChangeLanguagesActionSchema",
    "ProjectChangeMessagesConfigurationActionSchema",
    "ProjectChangeMessagesEnabledActionSchema",
    "ProjectChangeNameActionSchema",
    "ProjectSchema",
    "ProjectSetExternalOAuthActionSchema",
    "ProjectSetShippingRateInputTypeActionSchema",
    "ProjectUpdateActionSchema",
    "ProjectUpdateSchema",
    "ShippingRateInputTypeSchema",
]


class ExternalOAuthSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ExternalOAuth`."
    url = marshmallow.fields.String(allow_none=True)
    authorization_header = marshmallow.fields.String(
        allow_none=True, data_key="authorizationHeader"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ExternalOAuth(**data)


class ProjectSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.Project`."
    version = marshmallow.fields.Integer(allow_none=True)
    key = marshmallow.fields.String(allow_none=True)
    name = marshmallow.fields.String(allow_none=True)
    countries = marshmallow.fields.List(marshmallow.fields.String())
    currencies = marshmallow.fields.List(marshmallow.fields.String())
    languages = marshmallow.fields.List(marshmallow.fields.String())
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    trial_until = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="trialUntil"
    )
    messages = marshmallow.fields.Nested(
        nested="commercetools.schemas._message.MessageConfigurationSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    shipping_rate_input_type = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": "commercetools.schemas._project.CartClassificationTypeSchema",
            "CartScore": "commercetools.schemas._project.CartScoreTypeSchema",
            "CartValue": "commercetools.schemas._project.CartValueTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="shippingRateInputType",
    )
    external_o_auth = marshmallow.fields.Nested(
        nested="commercetools.schemas._project.ExternalOAuthSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="externalOAuth",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.Project(**data)


class ProjectUpdateActionSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ProjectUpdateAction`."
    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectUpdateAction(**data)


class ProjectUpdateSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ProjectUpdate`."
    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.Discriminator(
            discriminator_field=("action", "action"),
            discriminator_schemas={
                "changeCountries": "commercetools.schemas._project.ProjectChangeCountriesActionSchema",
                "changeCurrencies": "commercetools.schemas._project.ProjectChangeCurrenciesActionSchema",
                "changeLanguages": "commercetools.schemas._project.ProjectChangeLanguagesActionSchema",
                "changeMessagesConfiguration": "commercetools.schemas._project.ProjectChangeMessagesConfigurationActionSchema",
                "changeMessagesEnabled": "commercetools.schemas._project.ProjectChangeMessagesEnabledActionSchema",
                "changeName": "commercetools.schemas._project.ProjectChangeNameActionSchema",
                "setExternalOAuth": "commercetools.schemas._project.ProjectSetExternalOAuthActionSchema",
                "setShippingRateInputType": "commercetools.schemas._project.ProjectSetShippingRateInputTypeActionSchema",
            },
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        return types.ProjectUpdate(**data)


class ShippingRateInputTypeSchema(marshmallow.Schema):
    "Marshmallow schema for :class:`commercetools.types.ShippingRateInputType`."
    type = marshmallow_enum.EnumField(types.ShippingRateTierType, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.ShippingRateInputType(**data)


class CartClassificationTypeSchema(ShippingRateInputTypeSchema):
    "Marshmallow schema for :class:`commercetools.types.CartClassificationType`."
    values = marshmallow.fields.List(
        marshmallow.fields.Nested(
            nested="commercetools.schemas._type.CustomFieldLocalizedEnumValueSchema",
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartClassificationType(**data)


class CartScoreTypeSchema(ShippingRateInputTypeSchema):
    "Marshmallow schema for :class:`commercetools.types.CartScoreType`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartScoreType(**data)


class CartValueTypeSchema(ShippingRateInputTypeSchema):
    "Marshmallow schema for :class:`commercetools.types.CartValueType`."

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["type"]
        return types.CartValueType(**data)


class ProjectChangeCountriesActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeCountriesAction`."
    countries = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeCountriesAction(**data)


class ProjectChangeCurrenciesActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeCurrenciesAction`."
    currencies = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeCurrenciesAction(**data)


class ProjectChangeLanguagesActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeLanguagesAction`."
    languages = marshmallow.fields.List(marshmallow.fields.String())

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeLanguagesAction(**data)


class ProjectChangeMessagesConfigurationActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeMessagesConfigurationAction`."
    messages_configuration = marshmallow.fields.Nested(
        nested="commercetools.schemas._message.MessageConfigurationDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="messagesConfiguration",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeMessagesConfigurationAction(**data)


class ProjectChangeMessagesEnabledActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeMessagesEnabledAction`."
    messages_enabled = marshmallow.fields.Bool(
        allow_none=True, data_key="messagesEnabled"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeMessagesEnabledAction(**data)


class ProjectChangeNameActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectChangeNameAction`."
    name = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectChangeNameAction(**data)


class ProjectSetExternalOAuthActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectSetExternalOAuthAction`."
    external_o_auth = marshmallow.fields.Nested(
        nested="commercetools.schemas._project.ExternalOAuthSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="externalOAuth",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectSetExternalOAuthAction(**data)


class ProjectSetShippingRateInputTypeActionSchema(ProjectUpdateActionSchema):
    "Marshmallow schema for :class:`commercetools.types.ProjectSetShippingRateInputTypeAction`."
    shipping_rate_input_type = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "CartClassification": "commercetools.schemas._project.CartClassificationTypeSchema",
            "CartScore": "commercetools.schemas._project.CartScoreTypeSchema",
            "CartValue": "commercetools.schemas._project.CartValueTypeSchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="shippingRateInputType",
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data):
        del data["action"]
        return types.ProjectSetShippingRateInputTypeAction(**data)

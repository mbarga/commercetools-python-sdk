# DO NOT EDIT! This file is automatically generated

import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import LoggedResource, PagedQueryResponse

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, Reference
__all__ = [
    "Extension",
    "ExtensionAWSLambdaDestination",
    "ExtensionAction",
    "ExtensionAuthorizationHeaderAuthentication",
    "ExtensionAzureFunctionsAuthentication",
    "ExtensionChangeDestinationAction",
    "ExtensionChangeTriggersAction",
    "ExtensionDestination",
    "ExtensionDraft",
    "ExtensionHttpDestination",
    "ExtensionHttpDestinationAuthentication",
    "ExtensionInput",
    "ExtensionPagedQueryResponse",
    "ExtensionResourceTypeId",
    "ExtensionSetKeyAction",
    "ExtensionSetTimeoutInMsAction",
    "ExtensionTrigger",
    "ExtensionUpdate",
    "ExtensionUpdateAction",
]


class Extension(LoggedResource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.ExtensionDestination`
    destination: typing.Optional["ExtensionDestination"]
    #: List of :class:`commercetools.types.ExtensionTrigger`
    triggers: typing.Optional[typing.List["ExtensionTrigger"]]
    #: Optional :class:`int` `(Named` ``timeoutInMs`` `in Commercetools)`
    timeout_in_ms: typing.Optional[int]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        destination: typing.Optional["ExtensionDestination"] = None,
        triggers: typing.Optional[typing.List["ExtensionTrigger"]] = None,
        timeout_in_ms: typing.Optional[int] = None
    ) -> None:
        self.key = key
        self.destination = destination
        self.triggers = triggers
        self.timeout_in_ms = timeout_in_ms
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
            last_modified_by=last_modified_by,
            created_by=created_by,
        )

    def __repr__(self) -> str:
        return (
            "Extension(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, destination=%r, triggers=%r, timeout_in_ms=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.destination,
                self.triggers,
                self.timeout_in_ms,
            )
        )


class ExtensionAction(enum.Enum):
    CREATE = "Create"
    UPDATE = "Update"


class ExtensionDestination(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionDestinationSchema`."
    #: :class:`str`
    type: typing.Optional[str]

    def __init__(self, *, type: typing.Optional[str] = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionDestination(type=%r)" % (self.type,)


class ExtensionDraft(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`commercetools.types.ExtensionDestination`
    destination: typing.Optional["ExtensionDestination"]
    #: List of :class:`commercetools.types.ExtensionTrigger`
    triggers: typing.Optional[typing.List["ExtensionTrigger"]]
    #: Optional :class:`int` `(Named` ``timeoutInMs`` `in Commercetools)`
    timeout_in_ms: typing.Optional[int]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        destination: typing.Optional["ExtensionDestination"] = None,
        triggers: typing.Optional[typing.List["ExtensionTrigger"]] = None,
        timeout_in_ms: typing.Optional[int] = None
    ) -> None:
        self.key = key
        self.destination = destination
        self.triggers = triggers
        self.timeout_in_ms = timeout_in_ms
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ExtensionDraft(key=%r, destination=%r, triggers=%r, timeout_in_ms=%r)"
            % (self.key, self.destination, self.triggers, self.timeout_in_ms)
        )


class ExtensionHttpDestinationAuthentication(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionHttpDestinationAuthenticationSchema`."
    #: :class:`str`
    type: typing.Optional[str]

    def __init__(self, *, type: typing.Optional[str] = None) -> None:
        self.type = type
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionHttpDestinationAuthentication(type=%r)" % (self.type,)


class ExtensionInput(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionInputSchema`."
    #: :class:`commercetools.types.ExtensionAction`
    action: typing.Optional["ExtensionAction"]
    #: :class:`commercetools.types.Reference`
    resource: typing.Optional["Reference"]

    def __init__(
        self,
        *,
        action: typing.Optional["ExtensionAction"] = None,
        resource: typing.Optional["Reference"] = None
    ) -> None:
        self.action = action
        self.resource = resource
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionInput(action=%r, resource=%r)" % (self.action, self.resource)


class ExtensionPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.Extension`
    results: typing.Optional[typing.Sequence["Extension"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Extension"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "ExtensionPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


class ExtensionResourceTypeId(enum.Enum):
    CART = "cart"
    ORDER = "order"
    PAYMENT = "payment"
    CUSTOMER = "customer"


class ExtensionTrigger(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionTriggerSchema`."
    #: :class:`commercetools.types.ExtensionResourceTypeId` `(Named` ``resourceTypeId`` `in Commercetools)`
    resource_type_id: typing.Optional["ExtensionResourceTypeId"]
    #: List of :class:`commercetools.types.ExtensionAction`
    actions: typing.Optional[typing.List["ExtensionAction"]]

    def __init__(
        self,
        *,
        resource_type_id: typing.Optional["ExtensionResourceTypeId"] = None,
        actions: typing.Optional[typing.List["ExtensionAction"]] = None
    ) -> None:
        self.resource_type_id = resource_type_id
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionTrigger(resource_type_id=%r, actions=%r)" % (
            self.resource_type_id,
            self.actions,
        )


class ExtensionUpdate(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionUpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionUpdate(version=%r, actions=%r)" % (self.version, self.actions)


class ExtensionUpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionUpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ExtensionUpdateAction(action=%r)" % (self.action,)


class ExtensionAWSLambdaDestination(ExtensionDestination):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionAWSLambdaDestinationSchema`."
    #: :class:`str`
    arn: typing.Optional[str]
    #: :class:`str` `(Named` ``accessKey`` `in Commercetools)`
    access_key: typing.Optional[str]
    #: :class:`str` `(Named` ``accessSecret`` `in Commercetools)`
    access_secret: typing.Optional[str]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        arn: typing.Optional[str] = None,
        access_key: typing.Optional[str] = None,
        access_secret: typing.Optional[str] = None
    ) -> None:
        self.arn = arn
        self.access_key = access_key
        self.access_secret = access_secret
        super().__init__(type="AWSLambda")

    def __repr__(self) -> str:
        return (
            "ExtensionAWSLambdaDestination(type=%r, arn=%r, access_key=%r, access_secret=%r)"
            % (self.type, self.arn, self.access_key, self.access_secret)
        )


class ExtensionAuthorizationHeaderAuthentication(
    ExtensionHttpDestinationAuthentication
):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionAuthorizationHeaderAuthenticationSchema`."
    #: :class:`str` `(Named` ``headerValue`` `in Commercetools)`
    header_value: typing.Optional[str]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        header_value: typing.Optional[str] = None
    ) -> None:
        self.header_value = header_value
        super().__init__(type="AuthorizationHeader")

    def __repr__(self) -> str:
        return (
            "ExtensionAuthorizationHeaderAuthentication(type=%r, header_value=%r)"
            % (self.type, self.header_value)
        )


class ExtensionAzureFunctionsAuthentication(ExtensionHttpDestinationAuthentication):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionAzureFunctionsAuthenticationSchema`."
    #: :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, type: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(type="AzureFunctions")

    def __repr__(self) -> str:
        return "ExtensionAzureFunctionsAuthentication(type=%r, key=%r)" % (
            self.type,
            self.key,
        )


class ExtensionChangeDestinationAction(ExtensionUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionChangeDestinationActionSchema`."
    #: :class:`commercetools.types.ExtensionDestination`
    destination: typing.Optional["ExtensionDestination"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        destination: typing.Optional["ExtensionDestination"] = None
    ) -> None:
        self.destination = destination
        super().__init__(action="changeDestination")

    def __repr__(self) -> str:
        return "ExtensionChangeDestinationAction(action=%r, destination=%r)" % (
            self.action,
            self.destination,
        )


class ExtensionChangeTriggersAction(ExtensionUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionChangeTriggersActionSchema`."
    #: List of :class:`commercetools.types.ExtensionTrigger`
    triggers: typing.Optional[typing.List["ExtensionTrigger"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        triggers: typing.Optional[typing.List["ExtensionTrigger"]] = None
    ) -> None:
        self.triggers = triggers
        super().__init__(action="changeTriggers")

    def __repr__(self) -> str:
        return "ExtensionChangeTriggersAction(action=%r, triggers=%r)" % (
            self.action,
            self.triggers,
        )


class ExtensionHttpDestination(ExtensionDestination):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionHttpDestinationSchema`."
    #: :class:`str`
    url: typing.Optional[str]
    #: Optional :class:`commercetools.types.ExtensionHttpDestinationAuthentication`
    authentication: typing.Optional["ExtensionHttpDestinationAuthentication"]

    def __init__(
        self,
        *,
        type: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        authentication: typing.Optional["ExtensionHttpDestinationAuthentication"] = None
    ) -> None:
        self.url = url
        self.authentication = authentication
        super().__init__(type="HTTP")

    def __repr__(self) -> str:
        return "ExtensionHttpDestination(type=%r, url=%r, authentication=%r)" % (
            self.type,
            self.url,
            self.authentication,
        )


class ExtensionSetKeyAction(ExtensionUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ExtensionSetKeyAction(action=%r, key=%r)" % (self.action, self.key)


class ExtensionSetTimeoutInMsAction(ExtensionUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.ExtensionSetTimeoutInMsActionSchema`."
    #: Optional :class:`int` `(Named` ``timeoutInMs`` `in Commercetools)`
    timeout_in_ms: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        timeout_in_ms: typing.Optional[int] = None
    ) -> None:
        self.timeout_in_ms = timeout_in_ms
        super().__init__(action="setTimeoutInMs")

    def __repr__(self) -> str:
        return "ExtensionSetTimeoutInMsAction(action=%r, timeout_in_ms=%r)" % (
            self.action,
            self.timeout_in_ms,
        )

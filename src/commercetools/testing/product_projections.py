import typing
import dateutil.parser
from commercetools import schemas, types
from commercetools.services.product_projections import ProductProjectionsQuerySchema
from commercetools.testing import utils
from commercetools.testing.abstract import ServiceBackend
from commercetools.testing.utils import create_commercetools_response


class ProductProjectionsBackend(ServiceBackend):
    service_path = "product-projections"
    _schema_query_params = ProductProjectionsQuerySchema

    def urls(self):
        return [
            ("^$", "GET", self.query),
            ("^search", "POST", self.search),
            ("^key=(?P<key>[^/]+)$", "GET", self.get_by_key),
            ("^(?P<id>[^/]+)$", "GET", self.get_by_id),
        ]

    def query(self, request):
        params = utils.parse_request_params(ProductProjectionsQuerySchema, request)
        results = [
            self._convert_product_projection(product, params["staged"])
            for product in self.model.objects.values()
        ]
        results = [x for x in results if x]
        if params.get("limit"):
            results = results[: params["limit"]]

        if params.get("expand"):
            expanded_results = []
            for result in results:
                expanded_results.append(self._expand(request, result))
            results = expanded_results

        data = {
            "count": len(results),
            "total": len(results),
            "offset": 0,
            "results": results,
        }
        content = schemas.ProductProjectionPagedQueryResponseSchema().dumps(data)
        return create_commercetools_response(request, text=content)

    def search(self, request):
        params = utils.parse_request_params(ProductProjectionsQuerySchema, request)
        results = [
            self._convert_product_projection(product, params["staged"])
            for product in self.model.objects.values()
        ]
        results = [x for x in results if x]
        if params.get("limit"):
            results = results[: params["limit"]]

        if params.get("expand"):
            expanded_results = []
            for result in results:
                expanded_results.append(self._expand(request, result))
            results = expanded_results

        data = {
            "count": len(results),
            "total": len(results),
            "offset": 0,
            "results": results,
        }
        content = schemas.ProductProjectionPagedQueryResponseSchema().dumps(data)
        return create_commercetools_response(request, text=content)

    def get_by_id(self, request, id):
        obj = self.model.get_by_id(id)
        if obj:
            expanded_obj = self._expand(request, obj)
            content = schemas.ProductProjectionSchema().dumps(expanded_obj)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def get_by_key(self, request, key):
        obj = self.model.get_by_key(key)
        if obj:
            expanded_obj = self._expand(request, obj)
            content = schemas.ProductProjectionSchema().dumps(expanded_obj)
            return create_commercetools_response(request, text=content)
        return create_commercetools_response(request, status_code=404)

    def _convert_product_projection(
        self, product: typing.Dict, staged: bool = False
    ) -> typing.Optional[typing.Dict]:
        """Convert a Product object to a ProductProjection object"""
        if product["masterData"] is None:
            return None

        if staged:
            data = product["masterData"]["staged"]
        else:
            data = product["masterData"]["current"]

        if data is None:
            return None

        return {
            "id": product["id"],
            "key": product["key"],
            "version": product["version"],
            "created_at": dateutil.parser.parse(product["createdAt"]),
            "last_modified_at": dateutil.parser.parse(product["lastModifiedAt"]),
            "product_type": product["productType"],
            "name": data["name"],
            "description": data["description"],
            "slug": data["slug"],
            "categories": data["categories"],
            "category_order_hints": data["categoryOrderHints"],
            "meta_title": data["metaTitle"],
            "meta_description": data["metaDescription"],
            "meta_keywords": data["metaKeywords"],
            "search_keywords": data["searchKeywords"],
            "has_staged_changes": product["masterData"]["hasStagedChanges"],
            "published": product["masterData"]["published"],
            "master_variant": data["masterVariant"],
            "variants": data["variants"],
            "tax_category": product["taxCategory"],
            "state": product["state"],
            "review_rating_statistics": product["reviewRatingStatistics"],
        }

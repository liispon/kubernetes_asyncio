# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1APIResource(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'categories': 'list[str]',
        'group': 'str',
        'kind': 'str',
        'name': 'str',
        'namespaced': 'bool',
        'short_names': 'list[str]',
        'singular_name': 'str',
        'verbs': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'group': 'group',
        'kind': 'kind',
        'name': 'name',
        'namespaced': 'namespaced',
        'short_names': 'shortNames',
        'singular_name': 'singularName',
        'verbs': 'verbs',
        'version': 'version'
    }

    def __init__(self, categories=None, group=None, kind=None, name=None, namespaced=None, short_names=None, singular_name=None, verbs=None, version=None):  # noqa: E501
        """V1APIResource - a model defined in Swagger"""  # noqa: E501

        self._categories = None
        self._group = None
        self._kind = None
        self._name = None
        self._namespaced = None
        self._short_names = None
        self._singular_name = None
        self._verbs = None
        self._version = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if group is not None:
            self.group = group
        self.kind = kind
        self.name = name
        self.namespaced = namespaced
        if short_names is not None:
            self.short_names = short_names
        self.singular_name = singular_name
        self.verbs = verbs
        if version is not None:
            self.version = version

    @property
    def categories(self):
        """Gets the categories of this V1APIResource.  # noqa: E501

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :return: The categories of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1APIResource.

        categories is a list of the grouped resources this resource belongs to (e.g. 'all')  # noqa: E501

        :param categories: The categories of this V1APIResource.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def group(self):
        """Gets the group of this V1APIResource.  # noqa: E501

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :return: The group of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1APIResource.

        group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\".  # noqa: E501

        :param group: The group of this V1APIResource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """Gets the kind of this V1APIResource.  # noqa: E501

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :return: The kind of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1APIResource.

        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')  # noqa: E501

        :param kind: The kind of this V1APIResource.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this V1APIResource.  # noqa: E501

        name is the plural name of the resource.  # noqa: E501

        :return: The name of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1APIResource.

        name is the plural name of the resource.  # noqa: E501

        :param name: The name of this V1APIResource.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def namespaced(self):
        """Gets the namespaced of this V1APIResource.  # noqa: E501

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :return: The namespaced of this V1APIResource.  # noqa: E501
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced):
        """Sets the namespaced of this V1APIResource.

        namespaced indicates if a resource is namespaced or not.  # noqa: E501

        :param namespaced: The namespaced of this V1APIResource.  # noqa: E501
        :type: bool
        """
        if namespaced is None:
            raise ValueError("Invalid value for `namespaced`, must not be `None`")  # noqa: E501

        self._namespaced = namespaced

    @property
    def short_names(self):
        """Gets the short_names of this V1APIResource.  # noqa: E501

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :return: The short_names of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._short_names

    @short_names.setter
    def short_names(self, short_names):
        """Sets the short_names of this V1APIResource.

        shortNames is a list of suggested short names of the resource.  # noqa: E501

        :param short_names: The short_names of this V1APIResource.  # noqa: E501
        :type: list[str]
        """

        self._short_names = short_names

    @property
    def singular_name(self):
        """Gets the singular_name of this V1APIResource.  # noqa: E501

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :return: The singular_name of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._singular_name

    @singular_name.setter
    def singular_name(self, singular_name):
        """Sets the singular_name of this V1APIResource.

        singularName is the singular name of the resource.  This allows clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface.  # noqa: E501

        :param singular_name: The singular_name of this V1APIResource.  # noqa: E501
        :type: str
        """
        if singular_name is None:
            raise ValueError("Invalid value for `singular_name`, must not be `None`")  # noqa: E501

        self._singular_name = singular_name

    @property
    def verbs(self):
        """Gets the verbs of this V1APIResource.  # noqa: E501

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :return: The verbs of this V1APIResource.  # noqa: E501
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """Sets the verbs of this V1APIResource.

        verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy)  # noqa: E501

        :param verbs: The verbs of this V1APIResource.  # noqa: E501
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")  # noqa: E501

        self._verbs = verbs

    @property
    def version(self):
        """Gets the version of this V1APIResource.  # noqa: E501

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :return: The version of this V1APIResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1APIResource.

        version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource's group)\".  # noqa: E501

        :param version: The version of this V1APIResource.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1APIResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

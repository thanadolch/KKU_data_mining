{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "main.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPIPpwG3sfVXamoUIZSZPU4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/thanadolch/KKU_data_mining/blob/master/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_oEkKtjhlIZe"
      },
      "source": [
        "#!/usr/bin/env python3\n",
        "# Copyright (c) Facebook, Inc. and its affiliates.\n",
        "\n",
        "from params import Video3dParamsParser\n",
        "from process import DatasetProcessor\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    parser = Video3dParamsParser()\n",
        "    params = parser.parse()\n",
        "\n",
        "    dp = DatasetProcessor()\n",
        "    dp.process(params)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
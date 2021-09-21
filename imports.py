import os
import io
import psutil
import inspect
import textwarp
import textwrap
import traceback
import contextlib
import urllib
import discord

from io import BytesIO
from contextlib import redirect_stdout
from discord.ext import commands
from utils import lists, permissions, http, default, argparser